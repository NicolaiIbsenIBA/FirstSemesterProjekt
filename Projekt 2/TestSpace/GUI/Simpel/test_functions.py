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

master = ctk.CTk()
frame = ctk.CTkFrame(master)
frame.pack()

def new_show_table(frame, data):
    table = ttk.Treeview(frame, height=25, columns=data.columns.str.capitalize().tolist(), show='headings')
    for header in data.columns.str.capitalize().tolist():
        table.heading(header, text=header, command=lambda _col=header: sort_treeview(table, _col, False))
        table.column(header, width=100, stretch=False)
    table.pack()

    for index, row in data.iterrows():
        table.insert('', 'end', values=row.tolist())

    table.bind('<Double-1>', lambda event: on_double_click(event, table, frame))

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
        l.sort(key=lambda x: int(x[0]), reverse=reverse)
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


my_tree = new_show_table(frame, ntdb.workers_data)


btn = ttk.Button(frame, text='Confirm changes', command=lambda: changes_made(ntdb.workers_data, get_table_as_dataframe(my_tree)))
btn.pack()

def changes_made(database, tabel):
    tabel.columns = tabel.columns.str.upper()
    print(database)
    print(tabel)
    if database.equals(tabel):
        print("No changes made")
    else:
        print("Changes made")
        diff = database.compare(tabel)
        print(diff)

master.mainloop()
