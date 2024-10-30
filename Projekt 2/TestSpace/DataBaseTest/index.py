import my_functions as mf
import my_classes as mc
import pandas as pd

try:
    mf.drop_table()
    print("Table dropped successfully")
except Exception as e:
    print(e)

try:
    mf.create_table()
    print("Table created successfully")
except Exception as e:
    print(e)

try:
    mf.insert_table()
    print("Data inserted successfully")
except Exception as e:
    print(e)

try:
    table_liste = mf.select_table()
    print("Data selected successfully")
    database_dataframe = pd.DataFrame(table_liste, columns=['MATERIAL_ID', 'MACHINE', 'PROCESS', 'COST', 'UNIT', 'DENSITY'])
except Exception as e:
    print(e)

list_of_objects = []
for index, row in database_dataframe.iterrows():
    list_of_objects.append(mc.ThreeDPrinting(row['MATERIAL_ID'], row['MACHINE'], row['PROCESS'], row['COST'], row['UNIT'], row['DENSITY']))

for obj in list_of_objects:
    print(obj.__str__())