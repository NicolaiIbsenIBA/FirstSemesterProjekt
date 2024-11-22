import sqlite3
import pandas as pd

con = sqlite3.connect('logs.db')

# Create table
def create_logs_table():
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS logs
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                user TEXT,
                action_type TEXT,
                creation_id INTEGER)''')
    con.commit()

def create_user_creation():
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS user_creation
                (creation_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_created TEXT)''')
    con.commit()

# Insert data
def insert_user_creation_logs(user, new_user):
    cur = con.cursor()

    cur.execute(f"INSERT INTO user_creation (user_created) VALUES ('{new_user}')")
    con.commit()
    
    cur.execute(f"SELECT creation_id FROM user_creation WHERE user_created = '{new_user}'")
    action_id = cur.fetchone()[0]

    print(user)
    print(action_id)
    cur.execute(f"INSERT INTO logs (user, action_type, creation_id) VALUES ('{user}', 'User creation', {action_id})")
    con.commit()

# Drop table
def drop_logs_table():
    cur = con.cursor()
    cur.execute('''DROP TABLE IF EXISTS logs''')
    con.commit()

def drop_user_creation_id():
    cur = con.cursor()
    cur.execute('''DROP TABLE IF EXISTS user_creation''')
    con.commit()

# Select data
def select_user_creation_logs():
    try:
        found = pd.read_sql_query('''SELECT logs.timestamp, logs.user, user_creation.user_created
                                  FROM logs
                                  INNER JOIN user_creation ON logs.creation_id = user_creation.creation_id
''', con)
        # print(found)
        return found
    except Exception as e:
        print(e)

# Restart logs
def restart_logs():
    drop_logs_table()
    drop_user_creation_id()
    create_logs_table()
    create_user_creation()

