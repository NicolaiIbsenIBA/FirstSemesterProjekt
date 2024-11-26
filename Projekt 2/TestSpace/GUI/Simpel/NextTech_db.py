import sqlite3 as sql
import pandas as pd

con = sql.connect(f'Simpel/nextTech.db')

# Data collections
material_specifications_data = pd.DataFrame({
    'materialId': ['ABS', 'Ultem', 'Clear Resin', 'Dental Model Resin', 'Accura Xtreme', 'Casting Resin', 'PA2200', 'PA12', 'Alumide', 'Ti6Al4V', 'SSL316', 'Problack 10'],
    'printType': ['Trådprint', 'Trådprint', 'Resinprint', 'Resinprint', 'Resinprint', 'Resinprint', 'Laser', 'Laser', 'Laser', 'Laser', 'Laser', 'Resinprint'],
    'machine': ['Ultimaker 3', 'Fortus 360mc', 'Form2', 'Form2', 'ProX 950', 'Form2', 'EOSINT P800', 'EOSINT P800', 'EOSINT P800', 'EOSm100 or 400-4', 'EOSm100 or 400-4', '3D Systems Figure 4'],
    'process': ['FFF', 'FDM', 'SLA', 'SLA', 'SLA', 'SLA', 'SLS', 'SLS', 'SLS', 'SLM', 'SLM', 'DLP'],
    'cost': [66.66, 343, 149, 149, 2800, 299, 67.5, 60, 50, 400, 30, 250],
    'unit': ['$/kg', 'unit', '$/L', '$/L', '$/10kg', '$/L', '$/kg', '$/kg', '$/kg', '$/kg', '$/kg', '$/kg'],
    'density': [1.1, 1.27, 1.18, 1.18, 1.18, 1.18, 0.93, 1.01, 1.36, 4.43, 8, 1.07]
})


workers_data = pd.DataFrame({
    'process': ['FFF', 'FDM', 'SLA', 'DLP', 'SLS', 'SLM', 'FFF', 'FDM', 'SLA', 'DLP', 'SLS', 'SLM', 'FFF', 'FDM', 'SLA', 'DLP', 'SLS', 'SLM'],
    'jobTitle': ['engineer', 'engineer', 'engineer', 'engineer', 'engineer', 'engineer', 'operator', 'operator', 'operator', 'operator', 'operator', 'operator', 'technician', 'technician', 'technician', 'technician', 'technician', 'technician'],
    'salary': [70, 70, 70, 70, 70, 70, 40, 40, 40, 50, 50, 50, 30, 30, 30, 30, 30, 30]
})

# Queries
# Select queries
def sql_select_material_specifications_data():
    try:
        return pd.read_sql_query('SELECT * FROM materialSpecifications', con)
    except Exception as e:
        print(e)

def sql_select_workers_data():
    try:
        return pd.read_sql_query('SELECT * FROM workers', con)
    except Exception as e:
        print(e)

def sql_select_process_by_printtype(printtype):
    try:
        return pd.read_sql_query(f"SELECT process FROM materialSpecifications WHERE printType = '{printtype}'", con)
    except Exception as e:
        print(e)

def sql_select_machine_by_process(process):
    try:
        return pd.read_sql_query(f"SELECT machine FROM materialSpecifications WHERE process = '{process}'", con)
    except Exception as e:
        print(e)

def sql_select_everything_by_machine(machine):
    try:
        return pd.read_sql_query(f"SELECT * FROM materialSpecifications WHERE machine = '{machine}'", con)
    except Exception as e:
        print(e)

def sql_select_material_by_machine(machine):
    try:
        return pd.read_sql_query(f"SELECT materialId FROM materialSpecifications WHERE machine = '{machine}'", con)
    except Exception as e:
        print(e)

# Insert queries
def sql_insert_material_specifications_data(query):
    try:
        query.to_sql('materialSpecifications', con, if_exists='append', index=False)
        con.commit()
    except Exception as e:
        print(e)

def sql_insert_workers_data(query):
    try:
        query.to_sql('workers', con, if_exists='append', index=False)
        con.commit()
    except Exception as e:
        print(e)
        raise NameError("Error in inserting workers data")

# Create queries
def sql_create_material_specifications_table():
    # Create table if it doesn't exist
    try:
        con.execute('''
            CREATE TABLE IF NOT EXISTS materialSpecifications (
                materialId TEXT PRIMARY KEY,
                printType TEXT NOT NULL,
                machine TEXT NOT NULL,
                process TEXT NOT NULL,
                cost REAL NOT NULL,
                unit TEXT NOT NULL,
                density REAL NOT NULL
            )
        ''')
        con.commit()
    except Exception as e:
        print(e)

def sql_create_workers_table():
    # Create table if it doesn't exist
    try:
        con.execute('''
            CREATE TABLE IF NOT EXISTS workers (
                process TEXT NOT NULL,
                jobTitle TEXT NOT NULL,
                salary FLOAT NOT NULL,
                PRIMARY KEY (process, jobTitle)
            )
        ''')
        con.commit()
    except Exception as e:
        print(e)

# Update queries
"""def sql_update_material_specifications_data(query):
    try:
        query.to_sql('materialSpecifications', con, if_exists='replace', index=False)
        con.commit()
    except Exception as e:
        print(e)

def sql_update_material_specifications_data(df):
    try:
        cursor = con.cursor()
        for _, row in df.iterrows():
            cursor.execute('''
                UPDATE materialSpecifications
                SET materialName = ?, density = ?
                WHERE materialId = ?
            ''', (row['materialName'], row['density'], row['materialId']))
        con.commit()
    except Exception as e:
        print(e)
"""
def sql_update_from_list(query):
    try:
        for i in query:
            print(i)
            con.execute(i)
            con.commit()
    except Exception as e:
        print(e)

# Drop queries
def sql_drop_material_specifications_table():
    try:
        con.execute('DROP TABLE materialSpecifications')
        con.commit()
    except Exception as e:
        print(e)

def sql_drop_workers_table():
    try:
        con.execute('DROP TABLE workers')
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