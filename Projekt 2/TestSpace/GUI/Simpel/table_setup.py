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
        table.column(col, anchor='center', width=100, stretch=True)

    for _, row in data.iterrows():
        values = row.tolist()
        table.insert('', 'end', values=values)
    
    # Add vertical scrollbar
    vsb = ctk.CTkScrollbar(frame, orientation="vertical", command=table.yview)
    table.configure(yscrollcommand=vsb.set)
    vsb.pack(side='right', fill='y')

    # Add horizontal scrollbar
    hsb = ctk.CTkScrollbar(frame, orientation="horizontal", command=table.xview)
    table.configure(xscrollcommand=hsb.set)
    hsb.pack(side='bottom', fill='x')

    if mn.user.admin:
        # Add button to save changes
        table.bind('<Double-1>', lambda event: on_double_click(event))
        save_button = ctk.CTkButton(frame, text='Save changes', 
                                    command=lambda: changes_made(data, get_table_as_dataframe(table)))
        save_button.pack(side='bottom')

    table.pack(fill='both', expand=True)

    def create_entry_widget(item, column, col_index):
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

    def on_double_click(event):
        item = table.selection()
        if not item:
            return  # Ignore double-clicks on column headers
        item = item[0]
        column = table.identify_column(event.x)
        row = table.identify_row(event.y)
        col_index = int(column.replace('#', '')) - 1
        if columns == mn.workers_columns and col_index == 2:
            create_entry_widget(item, column, col_index)
        elif columns == mn.material_columns and col_index == 4:
            create_entry_widget(item, column, col_index)

def sort_treeview(tree, col, reverse):
    l = [(tree.set(k, col), k) for k in tree.get_children('')]
    if col == 'Salary':
        l.sort(key=lambda x: float(x[0]), reverse=reverse)
    elif col == 'Cost':
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
    tabel.columns = tabel.columns.str.upper()  # Capitalize and replace spaces with underscores

    database_list = database.values.tolist()  # pd.dataframe to list
    tabel_list = tabel.values.tolist()

    for i in tabel_list:
        for j in range(len(i)):
            try:
                # Try to convert to integer
                i[j] = int(i[j])
            except ValueError:
                try:
                    # Try to convert to float if integer conversion fails
                    i[j] = float(i[j])
                except ValueError:
                    # If both conversions fail, leave the value as is
                    pass
    
    database_set = set(map(tuple, database_list))
    tabel_set = set(map(tuple, tabel_list))
    
    if database_set == tabel_set:
        print("No changes made")
    else:
        print("Changes made")
        if database.columns.str.capitalize().tolist() == mn.workers_columns:
            ntdb.sql_update_from_list(query_changes_made_workers(list(tabel_set.difference(database_set))))
        elif database.columns.str.capitalize().tolist() == mn.material_columns:
            ntdb.sql_update_from_list(query_changes_material_specifications(list(tabel_set.difference(database_set))))

def query_changes_made_workers(changes):
    query_list = []
    for i in changes:
        query_list.append(f"UPDATE workers SET SALARY = {i[2]} WHERE process = '{i[0]}' AND jobTitle = '{i[1]}'")
    return query_list

def query_changes_material_specifications(changes):
    query_list = []
    for i in changes:
        query_list.append(f"UPDATE materialSpecifications SET cost = {i[4]} WHERE materialId = '{i[0]}'")
    return query_list
    