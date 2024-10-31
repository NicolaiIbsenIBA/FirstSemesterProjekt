import my_functions as mf
import my_classes as mc
import my_queries as mq
import pandas as pd

list_of_tables = ['MACHINE', 'WORKERS']

mf.drop_table(list_of_tables)

mf.create_material_specifications_table()
mf.create_workers_table()

mf.insert_table(mq.insert_material_specifications_query())
mf.insert_table(mq.insert_workers_query())

table_liste = mf.select_table("MACHINE")
database_dataframe = pd.DataFrame(table_liste, columns=['MATERIAL_ID', 'MACHINE', 'PROCESS', 'COST', 'UNIT', 'DENSITY'])

print('')
print(database_dataframe)

print('')
for index, row in database_dataframe.iterrows():
    print(row['MATERIAL_ID'], row['MACHINE'], row['PROCESS'], row['COST'], row['UNIT'], row['DENSITY'])

list_of_objects = []
for index, row in database_dataframe.iterrows():
    list_of_objects.append(mc.ThreeDPrinting(row['MATERIAL_ID'], row['MACHINE'], row['PROCESS'], row['COST'], row['UNIT'], row['DENSITY']))

print('')
for obj in list_of_objects:
    print(obj.process)