import sqlite3 as sql
import pandas as pd
import classes as cl

con = sql.connect(f'Simpel/UserCredentials.db')

# Data collections
test_user = cl.Credentials("ADMIN", "ADMIN", True)

# Queries
# Select queries
# Check if user exists
def check_login(username, password):
    query = f"""SELECT USERNAME, ADMIN FROM USER_CREDENTIAL WHERE USERNAME = '{username}' AND PASSWORD = '{password}'"""
    df = pd.read_sql_query(query, con)
    if df.empty:
        return False
    else:
        return True

def get_labels():    
    query = f"""SELECT LABEL FROM LABEL"""
    df = pd.read_sql_query(query, con)
    return df['LABEL'].tolist()

#

# Insert queries
def insert_user(new_user):
    try:
        con.execute(f"""INSERT INTO USER_CREDENTIAL (USERNAME, PASSWORD, ADMIN) VALUES 
                    ('{new_user.USERNAME}', '{new_user.PASSWORD}', {new_user.ADMIN})""")
        con.commit()
        print(f"user {new_user.USERNAME} inserted")
    except Exception as e:
        print(e)
        con.rollback()

def insert_label(label):
    try:
        con.execute(f"""INSERT INTO LABEL (LABEL) VALUES ('{label}')""")
        con.commit()
        print(f"LABEL {label} inserted")
    except Exception as e:
        print(e)
        con.rollback()


# Create queries
def create_user_table():
    try:
        con.execute("""CREATE TABLE IF NOT EXISTS USER_CREDENTIAL (
                    USERNAME TEXT PRIMARY KEY, 
                    PASSWORD TEXT, 
                    ADMIN BOOLEAN)""")
        con.commit()
        print(f"user_table created")
    except Exception as e:
        print(e)
        con.rollback()

def create_label_table():
    try:
        con.execute("""CREATE TABLE IF NOT EXISTS LABEL (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                    LABEL TEXT)""")
        con.commit()
        print(f"LABEL_table created")
    except Exception as e:
        print(e)
        con.rollback()

# Drop queries
def drop_user_table():
    try:
        con.execute("""DROP TABLE IF EXISTS USER_CREDENTIAL""")
        con.commit()
        print(f"user_table dropped")
    except Exception as e:
        print(e)
        con.rollback()

def drop_label_table():
    try:
        con.execute("""DROP TABLE IF EXISTS LABEL""")
        con.commit()
        print(f"LABEL_table dropped")
    except Exception as e:
        print(e)
        con.rollback()