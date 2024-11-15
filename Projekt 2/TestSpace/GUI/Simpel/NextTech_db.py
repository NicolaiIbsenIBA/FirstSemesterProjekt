import sqlite3 as sql
import pandas as pd

con = sql.connect(f'Simpel/NextTech.db')

# Data collections
material_specifications_data = pd.DataFrame ({
    'MATERIAL_ID': ['ABS', 'Ultem', 'Clear Resin', 'Dental Model Resin', 'Accura Xtreme', 'Casting Resin', 'PA2200', 'PA12', 'Alumide', 'Ti6Al4V', 'SSL316', 'Problack 10'],
    'MACHINE': ['Ultimaker 3', 'Fortus 360mc', 'Form2', 'Form2', 'ProX 950', 'Form2', 'EOSINT P800', 'EOSINT P800', 'EOSINT P800', 'EOSm100 or 400-4', 'EOSm100 or 400-4', '3D Systems Figure 4'],
    'PROCESS': ['FDM', 'FDM', 'SLA', 'SLA', 'SLA', 'SLA', 'SLS', 'SLS', 'SLS', 'SLM', 'SLM', 'DLP'],
    'COST': [66.66, 343, 149, 149, 2800, 299, 67.5, 60, 50, 400, 30, 250],
    'UNIT': ['$/kg', 'unit', '$/L', '$/L', '$/10kg', '$/L', '$/kg', '$/kg', '$/kg', '$/kg', '$/kg', '$/kg'],
    'DENSITY': [1.1, 1.27, 1.18, 1.18, 1.18, 1.18, 0.93, 1.01, 1.36, 4.43, 8, 1.07]
})

workers_data = pd.DataFrame ({
    'PROCESS': ['FFF', 'FDM', 'SLA', 'DLP', 'SLS', 'SLM','FFF', 'FDM', 'SLA', 'DLP', 'SLS', 'SLM','FFF', 'FDM', 'SLA', 'DLP', 'SLS', 'SLM'],
    'JOB_TITLE': ['engineer', 'engineer', 'engineer', 'engineer', 'engineer', 'engineer', 'operator', 'operator', 'operator', 'operator', 'operator', 'operator', 'technician', 'technician', 'technician', 'technician', 'technician', 'technician'],
    'SALARY': [70, 70, 70, 70, 70, 70, 40, 40, 40, 50, 50, 50, 30, 30, 30, 30, 30, 30]
})

# Queries
# Select queries
def sql_select_material_specifications_data():
    try:
        return pd.read_sql_query('SELECT * FROM MATERIAL_SPECIFICATIONS', con)
    except Exception as e:
        print(e)

def sql_select_workers_data():
    try:
        return pd.read_sql_query('SELECT * FROM WORKERS', con)
    except Exception as e:
        print(e)

# Insert queries
def sql_insert_material_specifications_data(query):
    try:
        query.to_sql('MATERIAL_SPECIFICATIONS', con, if_exists='append', index=False)
        con.commit()
    except Exception as e:
        print(e)

def sql_insert_workers_data(query):
    try:
        query.to_sql('WORKERS', con, if_exists='append', index=False)
        con.commit()
    except Exception as e:
        print(e)
        raise NameError("Error in inserting workers data")

# Create queries
def sql_create_material_specifications_table():
    # Create table if it doesn't exist
    try:
        con.execute('''
            CREATE TABLE IF NOT EXISTS MATERIAL_SPECIFICATIONS (
                MATERIAL_ID TEXT PRIMARY KEY,
                MACHINE TEXT NOT NULL,
                PROCESS TEXT NOT NULL,
                COST REAL NOT NULL,
                UNIT TEXT NOT NULL,
                DENSITY REAL NOT NULL
            )
        ''')
        con.commit()
    except Exception as e:
        print(e)

def sql_create_workers_table():
    # Create table if it doesn't exist
    try:
        con.execute('''
            CREATE TABLE IF NOT EXISTS WORKERS (
                PROCESS TEXT NOT NULL,
                JOB_TITLE TEXT NOT NULL,
                SALARY FLOAT NOT NULL,
                PRIMARY KEY (PROCESS, JOB_TITLE)
            )
        ''')
        con.commit()
    except Exception as e:
        print(e)

# Update queries
def sql_update_material_specifications_data(query):
    try:
        query.to_sql('MATERIAL_SPECIFICATIONS', con, if_exists='replace', index=False)
        con.commit()
    except Exception as e:
        print(e)

def sql_update_material_specifications_data(df):
    try:
        cursor = con.cursor()
        for _, row in df.iterrows():
            cursor.execute('''
                UPDATE MATERIAL_SPECIFICATIONS
                SET MaterialName = ?, Density = ?, TensileStrength = ?
                WHERE MaterialID = ?
            ''', (row['MaterialName'], row['Density'], row['TensileStrength'], row['MaterialID']))
        con.commit()
    except Exception as e:
        print(e)

def sql_update_workers_data(query):
    try:
        for i in query:
            con.execute(i)
            con.commit()
    except Exception as e:
        print(e)

# Drop queries
def sql_drop_material_specifications_table():
    try:
        con.execute('DROP TABLE MATERIAL_SPECIFICATIONS')
        con.commit()
    except Exception as e:
        print(e)

def sql_drop_workers_table():
    try:
        con.execute('DROP TABLE WORKERS')
        con.commit()
    except Exception as e:
        print(e)

# Restart tables
def restart_material_specifications_table():
    sql_drop_material_specifications_table()
    sql_create_material_specifications_table()
    sql_insert_material_specifications_data(material_specifications_data)

def restart_workers_table():
    sql_drop_workers_table()
    sql_create_workers_table()
    sql_insert_workers_data(workers_data)

def restart_tables_NextTech_db():
    restart_material_specifications_table()
    restart_workers_table()

# Call functions
# restart_material_specifications_table()
# restart_workers_table()