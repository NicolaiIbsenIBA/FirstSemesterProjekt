import sqlite3 as sql
import my_names as my_n

name_of_database = 'NEXTTECH_3D_PRINTING'
material_specifications_table = 'MACHINE'
workers_table = 'WORKERS'

con = sql.connect(f'{name_of_database}.db')

def create_material_specifications_table():
    try:
        con.execute(f"""CREATE TABLE {material_specifications_table} (
                    MATERIAL_ID TEXT PRIMARY KEY, 
                    MACHINE TEXT, 
                    PROCESS TEXT,
                    COST FLOAT,
                    UNIT TEXT,
                    DENSITY TEXT);""")
        con.commit()  
        print(f"'{material_specifications_table}' table created successfully")
    except Exception as e:
        print(e)

def create_workers_table():
    try:
        con.execute(f"""CREATE TABLE {workers_table} (
                        PROCESS TEXT,
                        JOB_TITLE TEXT,
                        SALARY TEXT,
                        PRIMARY KEY (PROCESS, JOB_TITLE)
                    );""")
        con.commit()
        print(f"'{workers_table}' table created successfully")
    except Exception as e:
        print(e)

def drop_table(table_list):
    try:
        for table in table_list:
            con.execute(f"DROP TABLE {table}")
            con.commit()
            print(f"'{table}' table dropped successfully")
    except Exception as e:
        print(e)

def insert_table(insert_query):
    try:
        con.execute(insert_query)
        con.commit()
    except Exception as e:
        print(e)

def select_table(table_name):
    try:
        cursor = con.execute(f"SELECT * FROM {table_name}")
        print(f"Data from '{table_name}' table selected successfully")
        return cursor.fetchall()
    except Exception as e:
        print(e)

