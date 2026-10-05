import mysql.connector
from mysql.connector import Error


DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "your_password",
    "database": "lost_and_found_db",
    "port": 3306
}

def get_connection():
    """
    Establishes and returns a connection to the MySQL database.
    Returns:
        mysql.connector.connection_cext.CMySQLConnection: Connection object if successful, None otherwise.
    """
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error connecting to MySQL Database: {e}")
        return None