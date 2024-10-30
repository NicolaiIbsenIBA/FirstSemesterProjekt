import pandas as pd

process_list = pd.DataFrame ({
    'MATERIAL_ID': ['ABS', 'Ultem', 'Clear Resin', 'Dental Model Resin', 'Accura Xtreme', 'Casting Resin', 'PA2200', 'PA12', 'Alumide', 'Ti6Al4V', 'SSL316', 'Problack 10'],
    'MACHINE': ['Ultimaker 3', 'Fortus 360mc', 'Form2', 'Form2', 'ProX 950', 'Form2', 'EOSINT P800', 'EOSINT P800', 'EOSINT P800', 'EOSm100 or 400-4', 'EOSm100 or 400-4', '3D Systems Figure 4'],
    'PROCESS': ['FDM', 'FDM', 'SLA', 'SLA', 'SLA', 'SLA', 'SLS', 'SLS', 'SLS', 'SLM', 'SLM', 'DLP'],
    'COST': [66.66, 343, 149, 149, 2800, 299, 67.5, 60, 50, 400, 30, 250],
    'UNIT': ['$/kg', 'unit', '$/L', '$/L', '$/10kg', '$/L', '$/kg', '$/kg', '$/kg', '$/kg', '$/kg', '$/kg'],
    'DENSITY': ['1,1', '1,27', '1,18', '1,18', '1,18', '1,18', '0,93', '1,01', '1,36', '4,43', '8', '1,07']
})

def insert_query():
    my_insert_query = f"""INSERT INTO my_table (MATERIAL_ID, MACHINE, PROCESS, COST, UNIT, DENSITY) VALUES"""
    for index, row in process_list.iterrows():
        my_insert_query += f""" ('{row['MATERIAL_ID']}', '{row['MACHINE']}', '{row['PROCESS']}', {row['COST']}, '{row['UNIT']}', '{row['DENSITY']}'),"""
    return (my_insert_query)[:-1]