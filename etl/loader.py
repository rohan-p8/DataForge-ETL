from pathlib import Path
import logging
from utils.logger import logger
import pandas as pd
from mysql.connector import Error



def save_processed_csv(dataframe: pd.DataFrame, output_path: Path) -> None:
    """
    Saves the processed DataFrame to a CSV file at the specified output path.
    """
    
    # Create the output directory if it doesn't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    dataframe.to_csv(output_path, index=False)

    
    logger.info(f"Processed file saved to: {output_path}")  


def insert_customers(connection, dataframe):
    """
    Inserts customer data from the DataFrame into the customers table.
    """
    try:
        cursor = connection.cursor()
        
        query = """
        INSERT IGNORE INTO customers(customer_id, customer_name)
        VALUES (%s, %s)
        """
        customer_data = []

        for _, row in dataframe.iterrows():
            
            customer_data.append(
                (
                    row['customer_id'],
                    row['customer_name'],
                )
            )
    
        cursor.executemany(query, customer_data)
        
        connection.commit()

        logger.info("Customers inserted successfully into the database.")

    except Error as e:
        
        logger.error(f"Error inserting customers: {e}")

def insert_products(connection, dataframe):
    """
    Inserts unique products into the products table.
    """
    try:
        cursor = connection.cursor()

        query = """
        INSERT IGNORE INTO products
        (product_name)
        VALUES (%s)
        """

        product_data = []

        unique_products = dataframe['product_name'].drop_duplicates()

        for product in unique_products:
            product_data.append((product,))

        cursor.executemany(query, product_data)
        
        connection.commit()

        logger.info("Products inserted successfully into the database.")

    except Error as e:
        logger.error(f"Error inserting products: {e}")



def insert_transactions(connection, dataframe: pd.DataFrame) -> None:
    """
    Inserts transaction data from the DataFrame into the transactions table.
    """

    try:
        cursor = connection.cursor()

        # Load all products once
        cursor.execute("""
                       SELECT product_id, product_name 
                       FROM products""")

        product_map = {}

        for product_id, product_name in cursor.fetchall():
            product_map[product_name] = product_id

        insert_query = """
        INSERT INTO transactions
        (
            transaction_id,
            customer_id,
            product_id,
            quantity,
            unit_price,
            transaction_date
        )
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        transaction_data = []

        for _, row in dataframe.iterrows():

            product_id = product_map.get(row['product_name'])

            if product_id is None:
                logger.error(
                    f"Product not found: {row['product_name']}"
                )
                continue

            transaction_data.append(
                (
                    row['transaction_id'],
                    row['customer_id'],
                    product_id,
                    row['quantity'],
                    row['unit_price'],
                    row['transaction_date']
                )
            )

        cursor.executemany(insert_query, transaction_data)

        connection.commit()

        logger.info("Transactions inserted successfully into the database.")

    except Error as e:
        logger.error(f"Error inserting transactions: {e}")
