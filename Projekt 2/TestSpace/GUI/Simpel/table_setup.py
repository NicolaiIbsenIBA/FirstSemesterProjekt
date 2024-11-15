import UserCredentials_db as udb
import NextTech_db as ntdb
import time
import pandas as pd
import sqlite3
import Datahandling as dh
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import my_names as mn
import NextTech_db as ntdb

def show_table(frame, data):
    columns = list(data.columns.str.capitalize().str.replace('_', ' '))
    table = ttk.Treeview(frame, columns=columns, show='headings', selectmode='browse')

    for col in columns:
        table.heading(col, text=col, command=lambda _col=col: sort_treeview(table, _col, False))
        table.column(col, anchor='center')

    for _, row in data.iterrows():
        values = row.tolist()
        # Format the 3rd entry to show only whole numbers
        values[2] = int(values[2])
        table.insert('', 'end', values=values)
    
    # Add vertical scrollbar
    vsb = ttk.Scrollbar(frame, orient="vertical", command=table.yview)
    table.configure(yscrollcommand=vsb.set)
    vsb.pack(side='right', fill='y')

    table.pack(fill='both', expand=True)

    if mn.user.admin:
        # Add button to save changes
        table.bind('<Double-1>', lambda event: on_double_click(event, table, frame))
        save_button = ctk.CTkButton(frame, text='Save changes', 
                                    command=lambda: changes_made(data, get_table_as_dataframe(table)))
        save_button.pack(side='bottom')
    return table

def on_double_click(event, table, frame):
    item = table.selection()[0]
    column = table.identify_column(event.x)
    row = table.identify_row(event.y)
    col_index = int(column.replace('#', '')) - 1
    if col_index == 2:  # Only allow editing the Salary column
        x, y, width, height = table.bbox(item, column)
        entry = tk.Entry(frame)
        entry.place(x=x, y=y, width=width, height=height)
        entry.focus()
        entry.insert(0, table.item(item)['values'][col_index])

        def on_exit_of_entry(event):
            table.set(item, column=column, value=entry.get())
            entry.destroy()

        entry.bind('<Return>', on_exit_of_entry)
        entry.bind('<FocusOut>', on_exit_of_entry)

def sort_treeview(tree, col, reverse):
    l = [(tree.set(k, col), k) for k in tree.get_children('')]
    if col == 'Salary':
        l.sort(key=lambda x: float(x[0]), reverse=reverse)
    else:
        l.sort(reverse=reverse)

    for index, (val, k) in enumerate(l):
        tree.move(k, '', index)

    tree.heading(col, command=lambda: sort_treeview(tree, col, not reverse))

def get_table_as_dataframe(tree):
    data = []
    for row_id in tree.get_children():
        row = tree.item(row_id)['values']
        data.append(dict(zip(tree['columns'], row)))
    return pd.DataFrame(data)

def changes_made(database, tabel):
    tabel.columns = tabel.columns.str.upper()

    database_list = database.values.tolist()  # pd.dataframe to list
    tabel_list = tabel.values.tolist()

    for i in tabel_list:
        for j in i:
            if type(j) == float:
                j = int(j)

    database_set = set(map(tuple, database_list))
    tabel_set = set(map(tuple, tabel_list))

    if database_set == tabel_set:
        print("No changes made")
    else:
        print("Changes made")
        ntdb.sql_update_workers_data(create_query_changes_made(list(tabel_set.difference(database_set))))

def create_query_changes_made(changes):
    query_list = []
    for i in changes:
        query_list.append(f"UPDATE WORKERS SET SALARY = {i[2]} WHERE PROCESS = '{i[0]}' AND JOB_TITLE = '{i[1]}'")
    return query_list
    