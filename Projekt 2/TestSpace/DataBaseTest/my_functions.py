import sqlite3 as sql
import my_queries as mq

name_of_database = 'NEXTTECH_3D_PRINTING.db'

con = sql.connect(f'{name_of_database}')

def create_table():
    try:
        con.execute("""CREATE TABLE my_table (
                    MATERIAL_ID TEXT PRIMARY KEY, 
                    MACHINE TEXT, 
                    PROCESS TEXT,
                    COST FLOAT,
                    UNIT TEXT,
                    DENSITY TEXT);d""")
        con.commit()
    except Exception as e:
        print(e)

def drop_table():
    try:
        con.execute("DROP TABLE my_table")
        con.commit()
    except Exception as e:
        print(e)

def insert_table():
    try:
        con.execute(mq.insert_query())
        con.commit()
    except Exception as e:
        print(e)

def select_table():
    try:
        cursor = con.execute("SELECT * FROM my_table")
        return cursor.fetchall()
    except Exception as e:
        print(e)

