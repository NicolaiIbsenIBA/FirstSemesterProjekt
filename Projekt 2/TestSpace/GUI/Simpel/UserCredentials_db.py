import sqlite3 as sql
import pandas as pd
import classes as cl
import logs_db as ldb
import my_names as mn

con = sql.connect(f'Simpel/UserCredentials.db')

# Data collections

# Queries
# Select queries
# Check if user exists
def check_login(username, password):
    query = f"""SELECT username, admin FROM UserCredential WHERE username = '{username}' AND password = '{password}'"""
    df = pd.read_sql_query(query, con)
    if df.empty:
        return [False, "User not found"]
    else:
        return [True, df["admin"][0]]

def get_labels():    
    query = f"""SELECT label FROM Label"""
    df = pd.read_sql_query(query, con)
    return df['label'].tolist()

# Insert queries
def insert_user(username, password, admin):
    try:
        con.execute(f"""INSERT INTO UserCredential (username, password, admin) VALUES 
                    ('{username}', '{password}', {admin})""")
        con.commit()

        # Insert log
        ldb.insert_user_creation_logs(mn.user.username, username)

    except sql.IntegrityError as e:
        raise NameError("User already exists")
    except Exception as e:
        print(e)
        con.rollback()

def insert_label(labellist):
    try:
        query = "INSERT INTO Label (label) VALUES (?)"
        con.executemany(query, [(label,) for label in labellist])
        con.commit()
        print(f"Labels {labellist} inserted")
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

# Restart function
def restart_user_table():
    drop_user_table()
    create_user_table()
    insert_user("admin", "admin", True)

def restart_label_table():
    drop_label_table()
    create_label_table()
    insert_label(["Material Specifications", "Workers", "Machines", "Products", "Orders", "Settings", "Settings", "Settings", "Settings", "Settings", "Settings", "Settings"])

def restart_tables_UserCredentials_db():
    restart_user_table()
    restart_label_table()

# Call function
# restart_user_table()
# restart_label_table()