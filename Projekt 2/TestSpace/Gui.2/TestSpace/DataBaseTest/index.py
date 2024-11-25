import my_functions as mf
import my_classes as mc
import my_queries as mq
import my_names as mn
import pandas as pd

# Drop the tables if they exist
list_of_tables = [mn.material_specifications_table, mn.workers_table]
mf.drop_table(list_of_tables)

# Create the tables
mf.create_material_specifications_table()
mf.create_workers_table()

# Insert data into the tables
mf.insert_table(mq.insert_material_specifications_query())
mf.insert_table(mq.insert_workers_query())

print("")
# Select the data from the tables and create dataframes
table_machine_list = mf.select_table(mn.material_specifications_table)
table_machines_dataframe = pd.DataFrame(table_machine_list, columns=['MATERIAL_ID', 'MACHINE', 'PROCESS', 'COST', 'UNIT', 'DENSITY'])

table_workers_list = mf.select_table(mn.workers_table)
table_workers_dataframe = pd.DataFrame(table_workers_list, columns=['PROCESS', 'JOB_TITLE', 'SALARY'])

print("")

# Create a list of machine objects and worker objects using my_classes and filling them with the data from the dataframes
list_of_machines = []
for index, row in table_machines_dataframe.iterrows():
    list_of_machines.append(mc.ThreeDPrinting(row['MATERIAL_ID'], row['MACHINE'], row['PROCESS'], row['COST'], row['UNIT'], row['DENSITY']))

list_of_workers = []
for index, row in table_workers_dataframe.iterrows():
    list_of_workers.append(mc.Worker(row['PROCESS'], row['JOB_TITLE'], row['SALARY']))

# Print the list of machines and workers
# print(*list_of_machines, sep="\n")
# print(*list_of_workers, sep="\n")

# A testloop
mf.my_loop()