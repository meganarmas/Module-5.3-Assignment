import mysql.connector
from mysql.connector import Error


def connect_database():
    db_name = "Gym_Database"
    user = "root"
    password = "hiddenpassword
    host = "localhost"

    try:
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )
        if conn.is_connected():
            print("Connected to MySQL database successfully.")
            return conn

    except Error as e:
        print(f"Error: {e}")
