import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password,
            database = db_name
        )
        print ("Connection to MySQL DB successful")
    except Error as e:
        print (f"Whoopsies! You got a {e}")
    return connection

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print ("Database created successfully")
    except Error as e:
        print ("another {e} lmao")

connection = create_connection("localhost", "root", "", "TheMagnusDatabase")
create_db_query = "CREATE DATABASE TheMagnusDatabase"
create_database(connection, create_db_query)
