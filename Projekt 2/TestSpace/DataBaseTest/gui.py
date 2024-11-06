from tkinter import *
import customtkinter as ctk
import CTkTable as ctktable

import my_queries as mq

master = ctk.CTk()
master.title("Custom Tkinter")
master.geometry("400x400")

textbox1 = ctk.CTkTextbox(master)
textbox1.insert(END, mq.workers_data)
textbox2 = ctk.CTkTextbox(master)
textbox2.insert(END, mq.material_specifications_data)

table = ctktable.CTkTable(master=master, row=3, column=5, values=mq.workers_data_list)

tabel1 = ctktable.CTkTable(master)

table.pack()

tabel1.pack()
textbox1.pack()
textbox2.pack()

master.mainloop()