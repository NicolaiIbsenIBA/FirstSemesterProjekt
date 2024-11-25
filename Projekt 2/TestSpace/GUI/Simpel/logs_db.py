import sqlite3
import pandas as pd

con = sqlite3.connect('Simpel/logs.db')

# Create table
def create_logs_table():
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS LOGS
                (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                TIMESTAMP DATETIME DEFAULT CURRENT_TIMESTAMP,
                USER TEXT,
                ACTION_TYPE TEXT,
                CREATION_ID INTEGER)''')
    con.commit()

def create_user_creation():
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS USER_CREATION
                (CREATION_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                USER_CREATED TEXT)''')
    con.commit()

# Insert data
def insert_user_creation_logs(USER, new_USER):
    cur = con.cursor()

    cur.execute(f"INSERT INTO USER_CREATION (USER_CREATED) VALUES ('{new_USER}')")
    con.commit()
    
    cur.execute(f"SELECT CREATION_ID FROM USER_CREATION WHERE USER_CREATED = '{new_USER}'")
    action_ID = cur.fetchone()[0]
    
    cur.execute(f"INSERT INTO LOGS (USER, ACTION_TYPE, CREATION_ID) VALUES ('{USER}', 'USER creation', {action_ID})")
    con.commit()

# Drop table
def drop_logs_table():
    cur = con.cursor()
    cur.execute('''DROP TABLE IF EXISTS LOGS''')
    con.commit()

def drop_user_creation_id():
    cur = con.cursor()
    cur.execute('''DROP TABLE IF EXISTS USER_CREATION''')
    con.commit()

# Select data
def select_user_creation_logs():
    try:
        found = pd.read_sql_query('''
            SELECT LOGS.TIMESTAMP, LOGS.USER, USER_CREATION.USER_CREATED
            FROM LOGS
            INNER JOIN USER_CREATION ON LOGS.CREATION_ID = USER_CREATION.CREATION_ID
            ORDER BY LOGS.TIMESTAMP DESC
        ''', con)
        # print(found)
        return found
    except Exception as e:
        print(e)

# Restart LOGS
def restart_logs():
    drop_logs_table()
    drop_user_creation_id()
    create_logs_table()
    create_user_creation()

