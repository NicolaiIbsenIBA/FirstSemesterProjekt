import sqlite3 as sql
import my_names as mn
import my_classes as mc

con = sql.connect(f'{mn.name_of_database}.db')

def create_material_specifications_table():
    try:
        con.execute(f"""CREATE TABLE {mn.material_specifications_table} (
                    MATERIAL_ID TEXT PRIMARY KEY, 
                    MACHINE TEXT, 
                    PROCESS TEXT,
                    COST FLOAT,
                    UNIT TEXT,
                    DENSITY TEXT);""")
        con.commit()  
        print(f"'{mn.material_specifications_table}' table created successfully")
    except Exception as e:
        print(e)

def create_workers_table():
    try:
        con.execute(f"""CREATE TABLE {mn.workers_table} (
                        PROCESS TEXT,
                        JOB_TITLE TEXT,
                        SALARY TEXT,
                        PRIMARY KEY (PROCESS, JOB_TITLE)
                    );""")
        con.commit()
        print(f"'{mn.workers_table}' table created successfully")
    except Exception as e:
        print(e)

def drop_table(table_list):
    try:
        for table in table_list:
            con.execute(f"DROP TABLE {table}")
            con.commit()
            print(f"'{table}' table dropped successfully")
    except Exception as e:
        print(e)

def insert_table(insert_query):
    try:
        con.execute(insert_query)
        con.commit()
    except Exception as e:
        print(e)

def select_table(table_name):
    try:
        cursor = con.execute(f"SELECT * FROM {table_name}")
        print(f"Data from '{table_name}' table selected successfully")
        return cursor.fetchall()
    except Exception as e:
        print(e)

def query_table(query):
    try:
        cursor = con.execute(query)
        print(f"Query executed successfully")
        return cursor.fetchall()
    except Exception as e:
        print(e)

def options():
    print("\nOptions:")
    print("1. Find the cost of labour for a given process and number of workers.")
    print("2. Some option.")
    print("3. Some other option.")
    return input("Press q to quit: ")

def my_loop():
    inp = options()
    while inp != 'q':
        print("You entered: ", inp)
        # Find the cost of labour for a given process and number of workers.
        if inp == '1':
            process = input("Enter the process: ")
            if process.upper() not in ['FFF', 'FDM', 'SLA', 'DLP', 'SLS', 'SLM']:
                print("Not a valid process.\n")
            else:
                number_of_engineers = input("Enter the number of engineers: ")
                number_of_techinicians = input("Enter the number of technicians: ")
                number_of_operators = input("Enter the number of operators: ")
            
                table_output = query_table(f"""SELECT * FROM WORKERS WHERE PROCESS = '{process.upper()}'""")
    
                try:
                    # Example 1: Using the list_of_workers list and the worker class to calculate the hourly cost of labour force
                    list_of_workers = []
                    for row in table_output:
                        list_of_workers.append(mc.Worker(row[0], row[1], row[2]))
                    for worker in list_of_workers:
                        print(worker)
                    print(f"That means the hourly cost of labour force of {(int(number_of_engineers) + int(number_of_operators) + int(number_of_techinicians))} workers is for the given {process.upper()} process is: {int(number_of_engineers)*int(list_of_workers[0].salary) + int(number_of_techinicians)*int(list_of_workers[1].salary) + int(number_of_operators)*int(list_of_workers[2].salary)}$")
                    # Example 2: Using the direct table_output list to calculate the cost of labour force
                    # print(f"That means the hourly cost of labour force of {(int(number_of_engineers) + int(number_of_operators) + int(number_of_techinicians))} workers is for the given {process.upper()} process is: {int(number_of_engineers)*int(table_output[0][2]) + int(number_of_techinicians)*int(table_output[1][2]) + int(number_of_operators)*int(table_output[2][2])}$")
                except ValueError:
                    print(f"Please enter a whole numbers for each of the type of worker you need.")
                print("")

        inp = options()
            