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


connection = create_connection("test.db")

create_statements_table = """
CREATE TABLE IF NOT EXISTS statements(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    robinson_id INTEGER,
    synopsis VARCHAR (150)
);
"""

create_object_table = """
CREATE TABLE IF NOT EXISTS objects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description VARCHAR (150)
);
"""

create_character_table = """
CREATE TABLE IF NOT EXISTS characters (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description VARCHAR (150)
);
"""

create_location_table = """
CREATE TABLE IF NOT EXISTS locations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR (100)
);
"""

create_organisation_table = """
CREATE TABLE IF NOT EXISTS organisations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR (100),
    locus INT NOT NULL,
    FOREIGN KEY (locus) REFERENCES locations(id)
);
"""

create_stat_char_table = """
CREATE TABLE IF NOT EXISTS group_to_members (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    statement_id INT NOT NULL,
    character_id INT NOT NULL,
    FOREIGN KEY (statement_id) REFERENCES statements(id),
    FOREIGN KEY (character_id) REFERENCES characters(id)
);
"""

create_org_char_table = """
CREATE TABLE IF NOT EXISTS group_to_members (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    group_id INT,
    character_id INT,
    FOREIGN KEY (group_id) REFERENCES organisations(id),
    FOREIGN KEY (character_id) REFERENCES characters(id)
);
"""

execute_query (connection, create_statements_table)
execute_query (connection, create_object_table)
execute_query (connection, create_character_table)
execute_query (connection, create_location_table)
execute_query (connection, create_organisation_table)
execute_query (connection, create_stat_char_table)
execute_query (connection, create_org_char_table)

