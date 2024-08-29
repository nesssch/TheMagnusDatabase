import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
        
    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def many_to_many(name, table1, table2):
    return ('CREATE TABLE IF NOT EXISTS '+ name + ' (' 
        'id INTEGER PRIMARY KEY AUTOINCREMENT,' + table1 + '_id INT NOT NULL,' + table2 + '_id INT NOT NULL,' 
        'FOREIGN KEY (' + table1 + '_id) REFERENCES ' + table1 + '(id),' 
        'FOREIGN KEY (' + table2 + '_id) REFERENCES ' + table2 + '(id),' 
    ');')

connection = create_connection("test.db")

NAME_TO_QUERY = {
    "create statements table" : """
    CREATE TABLE IF NOT EXISTS statements(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        robinson_id INTEGER,
        synopsis VARCHAR (150)
    );
    """,
    "create_objects_table" : """
    CREATE TABLE IF NOT EXISTS objects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description VARCHAR (150)
    );
    """,
    "create_character_table" : """
    CREATE TABLE IF NOT EXISTS characters (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description VARCHAR (150)
    );
    """,
    "create_location_table" : """
    CREATE TABLE IF NOT EXISTS locations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (100)
    );
    """,
    "create_event_table" : """
    CREATE TABLE IF NOT EXISTS events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description VARCHAR (150),
        date DATE
    );
    """,
    "create_org_table" : """
    CREATE TABLE IF NOT EXISTS organisations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (100),
        locus INT NOT NULL,
        FOREIGN KEY (locus) REFERENCES locations(id)
    );
    """,
    "create_stat_char_table": many_to_many("statements_to_characters", "statements", "characters")
}

print(many_to_many("org_to_char", "organisations", "characters"))

for query in NAME_TO_QUERY.values():
    execute_query (connection, query)


