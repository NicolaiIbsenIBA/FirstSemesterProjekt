import sqlite3
import pandas as pd

con = sqlite3.connect('Simpel/logs.db')

# Create table
def create_logs_table():
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS logs
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                user TEXT,
                actionType TEXT,
                creationId INTEGER)''')
    con.commit()

def create_user_creation():
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS userCreation
                (creationId INTEGER PRIMARY KEY AUTOINCREMENT,
                userCreated TEXT)''')
    con.commit()

# Insert data
def insert_user_creation_logs(user, new_user):
    cur = con.cursor()

    cur.execute("INSERT INTO userCreation (userCreated) VALUES (?)", (new_user,))
    con.commit()
    
    cur.execute("SELECT creationId FROM userCreation WHERE userCreated = ?", (new_user,))
    action_id = cur.fetchone()[0]
    
    cur.execute("INSERT INTO logs (user, actionType, creationId) VALUES (?, 'USER creation', ?)", (user, action_id))
    con.commit()

# Drop table
def drop_logs_table():
    cur = con.cursor()
    cur.execute('''DROP TABLE IF EXISTS logs''')
    con.commit()

def drop_user_creation_id():
    cur = con.cursor()
    cur.execute('''DROP TABLE IF EXISTS userCreation''')
    con.commit()

# Select data
def select_user_creation_logs():
    try:
        found = pd.read_sql_query('''
            SELECT logs.timestamp, logs.user, userCreation.userCreated
            FROM logs
            INNER JOIN userCreation ON logs.creationId = userCreation.creationId
            ORDER BY logs.timestamp DESC
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

