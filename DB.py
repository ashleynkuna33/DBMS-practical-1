import pymysql

STUDENT_NUMBER = "4429119"

DB_CONFIG = {
    "host": "172.21.12.21",
    "port": int(f"2{STUDENT_NUMBER[-4:]}"),
    "user": f"{STUDENT_NUMBER}",
    "password": f"!St{STUDENT_NUMBER}",
    "database": "lost_and_found_db",
    "cursorclass": pymysql.cursors.DictCursor,
}

def get_connection():
    """
    Establishes and returns a connection to the MySQL database.
    """
    try:
        connection = pymysql.connect(**DB_CONFIG)
        print("DB connected successfully!")
        return connection
    except Exception as e:
        print(f"Error connecting to MySQL Database: {e}")
        return None

# if __name__ == "__main__":
#     get_connection()