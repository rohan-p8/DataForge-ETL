import mysql.connector
from config.settings import DATABASE_CONFIG
from mysql.connector import Error


def get_connection():
    """
    Creates and return mysql database connection using the configuration 
    from settings.py
    """
    try:
        connection = mysql.connector.connect(
            host=DATABASE_CONFIG['host'],
            user=DATABASE_CONFIG['user'],
            password=DATABASE_CONFIG['password'],
            database=DATABASE_CONFIG['database']
        )

        if connection.is_connected():
            print("Successfully connected to the MySQL database")

        return connection
    
    except Error as e:
        print(f"Database connection error: {e}")
        return None