import mysql.connector
from mysql.connector import Error


def connect_database():
    db_name = "Managing_Fitness_Center_Database"
    user = "root"
    password = "********""
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
        print(f"Error {e}")
