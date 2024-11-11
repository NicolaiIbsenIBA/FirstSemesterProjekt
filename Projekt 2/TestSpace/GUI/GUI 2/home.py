import customtkinter as c
from tkinter import ttk  # Import ttk separately for Treeview
from tkinter import *  # Import ttk separately for Treeview
import my_queries as mq
import pandas as pd
from PIL import Image
import my_names as mn

def show_table(master, liste):
    # Create a Frame for the Treeview (for styling)
    frame1 = c.CTkFrame(master)
    frame1.pack(fill="both", padx= 20, pady=20)  # Pack the frame to make it visible

        # Create Treeview widget with scrollbars inside the CTk frame
    table = ttk.Treeview(frame1, columns=list(liste.columns), show="headings")

    # Define columns and headings
    for col in liste:
        table.heading(col, text=col, command=lambda _col=col: sort_table(_col, False))
        table.column(col, anchor="center", width=100)

    # Insert data into the Treeview
    for index, row in liste.iterrows():
        table.insert("", "end", values=list(row))
        
    # Pack the table and scrollbars in the frame
    table.pack(fill="both", padx= 8, pady=8)

    def sort_table(col, reverse):
        # Get the data from the Treeview
        data = [(table.set(child, col), child) for child in table.get_children('')]
        # Sort the data
        data.sort(reverse=reverse)
        # Rearrange the data in the Treeview
        for index, (val, child) in enumerate(data):
            table.move(child, '', index)
        # Reverse sort next time
        table.heading(col, command=lambda: sort_table(col, not reverse))
    
def label_gen(labels, frame):
    label_list = []
    i = 0
    j = 0
    while True:
        label_list.append(c.CTkLabel(frame, 
                                         text=labels['Settings'][i],
                                         font=("Arial", 12), 
                                         width=(frame._current_width/3), 
                                         fg_color=mn.black, 
                                         bg_color=mn.primary_grey))
        label_list[i].grid(row=j, column=(i-(3*j)), padx=2, pady=2)
        if ((i+1) / 3).is_integer():
            j+=1
        i+=1
        if labels['Settings'].__len__() == i:
            return label_list

def homepage_content(master):
    main_frame = c.CTkFrame(master, 
                                fg_color=mn.primary_grey, 
                                bg_color=mn.primary_grey, 
                                width=650,
                                border_color=mn.black, 
                                border_width=1,
                                corner_radius=0)

    labelgen = pd.DataFrame ({
            'Settings': ['Material Specifications', 'Workers', 'Machines', 'Products', 'Orders', 'Settings', 'Settings', 'Settings', 'Settings', 'Settings', 'Settings', 'Settings'],
    })
    label_list = label_gen(labelgen, main_frame)
    
    main_frame.pack(pady=20)
    calculator_content(master)

def calculator_content(master):
    
    calc_frame = c.CTkFrame(master, 
                                fg_color=mn.primary_grey, 
                                bg_color=mn.primary_grey, 
                                height=400,
                                width=650,
                                border_color=mn.black, 
                                border_width=1)
    calc_frame.pack(pady=20)

        # Big frame
    big_frame = c.CTkFrame(calc_frame, 
                                fg_color=mn.primary_grey, 
                                bg_color=mn.primary_grey, 
                                height=calc_frame._current_height,
                                width=calc_frame._current_width/3,
                                border_color=mn.black, 
                                border_width=1)

    smaller_frames = c.CTkFrame(calc_frame, 
                                    fg_color=mn.primary_grey, 
                                    bg_color=mn.primary_grey, 
                                    height=calc_frame._current_height,
                                    width=calc_frame._current_width/3,
                                    border_color=mn.black, 
                                    border_width=1)
        # Material frame
    material_frame = c.CTkFrame(smaller_frames, 
                                    fg_color=mn.primary_grey, 
                                    bg_color=mn.primary_grey, 
                                    height=smaller_frames._current_height/2,
                                    border_color=mn.black, 
                                    border_width=1)
        # Smaller frame
    small_frame = c.CTkFrame(smaller_frames, 
                                 fg_color=mn.primary_grey, 
                                 bg_color=mn.primary_grey, 
                                 height=smaller_frames._current_height/2,
                                 border_color=mn.black, 
                                 border_width=1)
        
    big_frame.grid(row=0, column=0, padx=5, pady=5)
    smaller_frames.grid(row=0, column=1, padx=5, pady=5)
    material_frame.pack()
    small_frame.pack()