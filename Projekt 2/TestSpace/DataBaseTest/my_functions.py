import sqlite3 as sql
import my_queries as mq

name_of_database = 'NEXTTECH_3D_PRINTING'

con = sql.connect(f'{name_of_database}.db')

def create_table():
    try:
        con.execute(f"""CREATE TABLE {name_of_database} (
                    MATERIAL_ID TEXT PRIMARY KEY, 
                    MACHINE TEXT, 
                    PROCESS TEXT,
                    COST FLOAT,
                    UNIT TEXT,
                    DENSITY TEXT);""")
        con.commit()
    except Exception as e:
        print(e)

def drop_table():
    try:
        con.execute(f"DROP TABLE {name_of_database}")
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
        cursor = con.execute(f"SELECT * FROM {name_of_database}")
        return cursor.fetchall()
    except Exception as e:
        print(e)

