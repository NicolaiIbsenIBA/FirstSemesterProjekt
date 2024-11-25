import sqlite3 as sql
import pandas as pd
import classes as cl
import logs_db as ldb
import my_names as mn

con = sql.connect(f'Simpel/user_credentials.db')

# Data collections

# Queries
# Select queries
# Check if user exists
def check_login(username, password):
    query = f"""SELECT USERNAME, ADMIN FROM USER_CREDENTIAL WHERE USERNAME = '{username}' AND PASSWORD = '{password}'"""
    df = pd.read_sql_query(query, con)
    if df.empty:
        return [False, "User not found"]
    else:
        return [True, df["ADMIN"][0]]

def get_labels():    
    query = f"""SELECT LABEL FROM LABEL"""
    df = pd.read_sql_query(query, con)
    return df['LABEL'].tolist()

# Insert queries
def insert_user(username, password, admin):
    try:
        con.execute(f"""INSERT INTO USER_CREDENTIAL (USERNAME, PASSWORD, ADMIN) VALUES 
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
        query = "INSERT INTO LABEL (LABEL) VALUES (?)"
        con.executemany(query, [(label,) for label in labellist])
        con.commit()
        print(f"Labels {labellist} inserted")
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

# Restart function
def restart_user_table():
    drop_user_table()
    create_user_table()
    print("")
    insert_user("admin", "admin", True)
    print("")

def restart_label_table():
    drop_label_table()
    create_label_table()
    insert_label(["Material Specifications", "Workers", "Machines", "Products", "Orders", "Settings", "Settings", "Settings", "Settings", "Settings", "Settings", "Settings"])

def restart_tables_users_db():
    restart_user_table()
    restart_label_table()

# Call function
# restart_user_table()
# restart_label_table()