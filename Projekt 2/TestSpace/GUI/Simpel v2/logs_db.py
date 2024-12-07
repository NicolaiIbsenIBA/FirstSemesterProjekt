import sqlite3
import pandas as pd
import my_names as mn

con = sqlite3.connect(mn.logs_db_path)

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

def create_raw_cost_calculation():
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS rawCostCalculation
                (creationId INTEGER PRIMARY KEY AUTOINCREMENT,
                machine TEXT,
                material TEXT,
                quantity REAL,
                unit TEXT,
                price REAL)''')
    con.commit()

# Insert data
def insert_user_creation_log(user, new_user):
    cur = con.cursor()

    cur.execute("INSERT INTO userCreation (userCreated) VALUES (?)", (new_user,))
    con.commit()
    
    cur.execute("SELECT creationId FROM userCreation WHERE userCreated = ?", (new_user,))
    action_id = cur.fetchone()[0]
    
    cur.execute("INSERT INTO logs (user, actionType, creationId) VALUES (?, 'user creation', ?)", (user, action_id))
    con.commit()

def insert_raw_cost_calculation_log(machine, material, quantity, unit, price):
    cur = con.cursor()

    cur.execute("INSERT INTO rawCostCalculation (machine, material, quantity, unit, price) VALUES (?, ?, ?, ?, ?)", (machine, material, quantity, unit, price))
    con.commit()
    
    cur.execute("SELECT creationId FROM rawCostCalculation WHERE machine = ? AND material = ? AND quantity = ? AND unit = ? AND price = ?", (machine, material, quantity, unit, price))
    action_id = cur.fetchone()[0]
    
    cur.execute("INSERT INTO logs (user, actionType, creationId) VALUES (?, 'raw cost calculation', ?)", (mn.user.username, action_id))
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

def drop_raw_cost_calculation():
    cur = con.cursor()
    cur.execute('''DROP TABLE IF EXISTS rawCostCalculation''')
    con.commit()

# Select data
def select_user_creation_logs():
    try:
        found = pd.read_sql_query('''
            SELECT logs.timestamp, logs.user, userCreation.userCreated
            FROM logs
            INNER JOIN userCreation ON logs.creationId = userCreation.creationId
            WHERE actionType = 'user creation'
            ORDER BY logs.timestamp DESC
        ''', con)
        # print(found)
        return found
    except Exception as e:
        print(e)

def select_raw_cost_calculation_logs():
    try:
        found = pd.read_sql_query('''
            SELECT rawCostCalculation.machine, rawCostCalculation.material, rawCostCalculation.quantity, rawCostCalculation.unit, rawCostCalculation.price
            FROM logs
            INNER JOIN rawCostCalculation ON logs.creationId = rawCostCalculation.creationId
            WHERE actionType = 'raw cost calculation'
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
    drop_raw_cost_calculation()
    create_logs_table()
    create_user_creation()
    create_raw_cost_calculation()

