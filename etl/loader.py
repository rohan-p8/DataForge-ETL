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

        for _, row in dataframe.iterrows():

            cursor.execute(
                query,
                (
                        row['customer_id'],
                        row['customer_name']
                ),
            )

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

        for _, row in dataframe.iterrows():
            cursor.execute(
                query,
                (
                    row['product_name'],
                ),
            )
        
        connection.commit()

        logger.info("Products inserted successfully into the database.")

    except Error as e:
        logger.error(f"Error inserting products: {e}")



def insert_transactions(connection, dataframe):
    """
    Inserts transaction data from the DataFrame into the transactions table.
    """

    try:
        cursor = connection.cursor()

        select_query = """
        SELECT product_id 
        FROM products 
        WHERE product_name = %s
        """

        insert_query = """
        INSERT INTO transactions
        (transaction_id, customer_id, product_id, quantity, 
        unit_price, transaction_date)
        VALUES (%s, %s, %s, %s, %s, %s)
        """


        for _, row in dataframe.iterrows():
            
            # Step 1: Find product_id
            cursor.execute(
                select_query,
                (row['product_name'],)
            )

            result = cursor.fetchone() # to retrieve one record product_id 

            if result is None:
                logger.error(
                    f"Product not found: {row['product_name']}"
                )
                continue

            product_id = result[0]

            # Step 2: Insert transaction
            cursor.execute(
                insert_query,
                (
                    row['transaction_id'],
                    row['customer_id'],
                    product_id,
                    row['quantity'],
                    row['unit_price'],
                    row['transaction_date']
                ),
            )

        connection.commit()
        
        logger.info("Transactions inserted successfully into the database.")


    except Error as e:
        logger.error(f"Error inserting transactions: {e}")


