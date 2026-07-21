from pathlib import Path

from config.database import get_connection

from etl.extractor import extract_csv, extract_json
from etl.validator import (
    validate_required_columns,
    validate_missing_values,
    validate_positive_numbers,
)

from etl.transformer import (
    standardize_column_names,
    remove_extra_spaces,
    convert_to_title_case,
    remove_duplicates,
)

from etl.loader import (
    save_processed_csv, 
    insert_customers,
    insert_products,
    insert_transactions
)

from utils.logger import logger

from config.settings import INPUT_FILE, OUTPUT_FILE



def main():

    connection = None

    try:

        logger.info("ETL Pipeline Started.")


        # Extract data from CSV file
        logger.info("Reading/extracting data from CSV file.")
        dataframe = extract_csv(INPUT_FILE)
        

        # Validate the extracted data
        logger.info("Validating extracted data.")
        validate_required_columns(dataframe)
        validate_missing_values(dataframe)
        validate_positive_numbers(dataframe)


        # Transform the data
        logger.info("Transforming data.")
        dataframe = standardize_column_names(dataframe)
        dataframe = remove_extra_spaces(dataframe)
        dataframe = convert_to_title_case(dataframe)
        dataframe = remove_duplicates(dataframe)


        # Load the processed data to a CSV file
        logger.info("Saving processed data to CSV file.")
        save_processed_csv(dataframe, OUTPUT_FILE)


        # Connect to the database MySQL
        logger.info("Connecting to the MySQL database.")
        connection = get_connection()

        if connection is not None:
            logger.info("Loading customers into the database.")
            insert_customers(connection, dataframe)
            logger.info("Loading products into the database.")
            insert_products(connection, dataframe)
            logger.info("Loading transactions into the database.")
            insert_transactions(connection, dataframe)

            # Commit the changes to the database
            connection.commit()  


             # Output
            logger.info("ETL Pipeline Completed Successfully.")
        
        
    except Exception as e:

        connection.rollback()
        logger.error("Rolling back the transaction due to an error.")
        logger.error(f"ETL Pipeline Failed: {e}")


    finally:
        if connection is not None:
            connection.close()
            logger.info("Database connection closed.")

if __name__ == "__main__":
    main()