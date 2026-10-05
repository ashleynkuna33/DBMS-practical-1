import mysql.connector
from mysql.connector import Error


STUDENT_NUMBER = "4429119"

DB_CONFIG = {
    "host": "172.21.12.21",
    "port": int(f"2{STUDENT_NUMBER[-4:]}"),
    "user": f"student_{STUDENT_NUMBER}",
    "password": f"!St{STUDENT_NUMBER}",
    "database": "lost_and_found_db",
    "ssl_mode": "REQUIRED",
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