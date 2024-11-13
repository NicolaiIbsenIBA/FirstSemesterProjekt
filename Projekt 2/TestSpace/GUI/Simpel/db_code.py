import sqlite3 as sql
import pandas as pd
import classes as cl

con = sql.connect(f'Simpel/UserCredentials.db')

# Data collections
test_user = cl.Credentials("admin", "admin", True)

# Queries
# Select queries
# Check if user exists
def check_login(username, password):
    query = f"""SELECT username, admin FROM UserCredential WHERE username = '{username}' AND password = '{password}'"""
    df = pd.read_sql_query(query, con)
    if df.empty:
        return False
    else:
        return True

def get_labels():    
    query = f"""SELECT label FROM Label"""
    df = pd.read_sql_query(query, con)
    return df['label'].tolist()

# Insert queries
def insert_user(new_user):
    try:
        con.execute(f"""INSERT INTO UserCredential (username, password, admin) VALUES 
                    ('{new_user.username}', '{new_user.password}', {new_user.admin})""")
        con.commit()
        print(f"user {new_user.username} inserted")
    except Exception as e:
        print(e)
        con.rollback()

def insert_label(label):
    try:
        con.execute(f"""INSERT INTO Label (label) VALUES ('{label}')""")
        con.commit()
        print(f"label {label} inserted")
    except Exception as e:
        print(e)
        con.rollback()


# Create queries
def create_user_table():
    try:
        con.execute("""CREATE TABLE IF NOT EXISTS UserCredential (
                    username TEXT PRIMARY KEY, 
                    password TEXT, 
                    admin BOOLEAN)""")
        con.commit()
        print(f"user_table created")
    except Exception as e:
        print(e)
        con.rollback()

def create_label_table():
    try:
        con.execute("""CREATE TABLE IF NOT EXISTS Label (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    label TEXT)""")
        con.commit()
        print(f"label_table created")
    except Exception as e:
        print(e)
        con.rollback()

# Drop queries
def drop_user_table():
    try:
        con.execute("""DROP TABLE IF EXISTS UserCredential""")
        con.commit()
        print(f"user_table dropped")
    except Exception as e:
        print(e)
        con.rollback()

def drop_label_table():
    try:
        con.execute("""DROP TABLE IF EXISTS Label""")
        con.commit()
        print(f"label_table dropped")
    except Exception as e:
        print(e)
        con.rollback()

drop_label_table()
create_label_table()
for i in range(10):
    insert_label(f"{i}")