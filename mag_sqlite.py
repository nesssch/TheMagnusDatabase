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
        'FOREIGN KEY (' + table2 + '_id) REFERENCES ' + table2 + '(id)' 
    ');')

connection = create_connection("test.db")

NAME_TO_QUERY = {
    "create statements table" : """
    CREATE TABLE IF NOT EXISTS statements(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        robinson_id INTEGER,
        date_given DATE,
        synopsis VARCHAR (150)
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
    "create_objects_table" : """
    CREATE TABLE IF NOT EXISTS objects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description VARCHAR (150),
        eff_id INT NOT NULL,
        FOREIGN KEY (eff_id) REFERENCES effects(id)
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
    "create_effect_table" : """
    CREATE TABLE IF NOT EXISTS events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description VARCHAR (150),
    );
    """,
    "create_stat_chr_table": many_to_many("stat_to_chr", "statements", "characters"),
    "create_stat_obj_table": many_to_many("stat_to_obj", "statements", "objects"),
    "create_stat_loc_table": many_to_many("stat_to_loc", "statements", "locations"),
    "create_stat_eff_table": many_to_many("stat_to_eff", "statements", "effects"),
    "create_stat_org_table": many_to_many("stat_to_org", "statements", "organisations"),
    "create_char_eff_table": many_to_many("char_to_eff", "characters", "effects"),
    "create_char_obj_table": many_to_many("char_to_obj", "characters", "objects"),
    "create_char_org_table": many_to_many("char_to_org", "characters", "organisations"),
    "create_obj_chr_table": many_to_many("obj_to_chr", "objects", "characters"),
    "create_obj_org_table": many_to_many("obj_to_org", "objects", "organisations"),
    "create_org_loc_table": many_to_many("org_to_loc", "organisations", "locations"),
    "create_org_eff_table": many_to_many("org_to_eff", "organisations", "effects")
}

# print(many_to_many("org_to_char", "organisations", "characters"))

for query in NAME_TO_QUERY.values():
    execute_query (connection, query)