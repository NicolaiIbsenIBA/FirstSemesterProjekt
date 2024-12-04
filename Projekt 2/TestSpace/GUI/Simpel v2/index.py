from tkinter import *
from tkinter import ttk
import customtkinter as ctk
import classes as cl
import my_names as mn
from PIL import Image
import UserCredentials_db as udb
import NextTech_db as ntdb
import time
import pandas as pd
import sqlite3
import Datahandling as dh
import table_setup as ts
import logs_db as ldb

# Declare variables
user = cl.Credentials(None, None, False)

# Functions
def greet_user():
    if user.username is None:
        print("Hello guest")
    else:
        print(f"Hello {user.username}")

# Test functions
def label_gen(frame, labels):
    labelframe = ctk.CTkFrame(frame,
                              width=400)
    labelframe.pack()
    label_list = []
    i = 0
    j = 0
    while True:
        label_list.append(ctk.CTkLabel(labelframe,
                                       text=labels[i],
                                       font=("Arial", 12), 
                                       width=(labelframe._current_width/3), 
                                       fg_color=mn.black, 
                                       bg_color=mn.primary_grey))
        label_list[i].grid(row=j, column=(i-(3*j)), padx=2, pady=2)
        if ((i+1) / 3).is_integer():
            j+=1
        i+=1
        if labels.__len__() == i:
            return label_list

def button_gen(frame, buttons):
    buttonframe = ctk.CTkFrame(frame,
                               width=400)
    buttonframe.pack()
    button_list = []
    i = 0
    j = 0
    while True:
        button_list.append(ctk.CTkButton(buttonframe,
                                         text=buttons[i],
                                         font=("Arial", 12),
                                         command=lambda: print(f"Button pressed"),
                                         fg_color=mn.black,
                                         bg_color=mn.primary_grey))
        button_list[i].grid(row=j, column=(i-(3*j)), padx=2, pady=2)
        if ((i+1) / 3).is_integer():
            j+=1
        i+=1
        if buttons.__len__() == i:
            return button_list

def decrepit_show_table(frame, liste):
        # Create a Frame for the Treeview (for styling)
        frame1 = ctk.CTkFrame(frame)
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

# Main window
master = ctk.CTk()
master.geometry("700x600")
master.iconbitmap(mn.ico_path)
master.title("NexText CALC")
master.configure(fg_color=mn.black, bg_color=mn.black)

# Header
header = ctk.CTkFrame(master,
                      bg_color=mn.black,
                      fg_color=mn.black)
header.custom_name = "header"
header.grid(row=0, column=0, sticky="nsew", columnspan=2)

header_frame_1 = ctk.CTkFrame(header, bg_color=mn.black, fg_color=mn.black)
header_frame_2 = ctk.CTkFrame(header, bg_color=mn.black, fg_color=mn.black)
header_frame_3 = ctk.CTkFrame(header, bg_color=mn.black, fg_color=mn.black)
header_frame_1.grid(row=0, column=0, sticky="w")
header_frame_2.grid(row=0, column=1)
header_frame_3.grid(row=0, column=2, sticky="e", padx=5)
header.grid_columnconfigure((0,1,2), weight=1, uniform="column")

icon = ctk.CTkImage(light_image=Image.open(mn.home_icon_path), size=(50, 50))
icon_label = ctk.CTkButton(header_frame_1, 
                           image=icon, 
                           command=lambda: home_page(main_frame), 
                           text="",
                           width=1,
                           bg_color=mn.black,
                           fg_color=mn.black)
icon_label.pack(padx=(45, 0), pady=(0,2))

logo = ctk.CTkImage(light_image=Image.open(mn.logo_path), size=(241, 55))
admin_logo = ctk.CTkImage(light_image=Image.open(mn.admin_logo_path), size=(241, 55))
logo_label = ctk.CTkLabel(header_frame_2, 
                          image=logo, 
                          text="")
logo_label.pack()

user_frame = ctk.CTkFrame(header_frame_3, 
                          width=0, 
                          height=0, 
                          bg_color=mn.black,
                          fg_color=mn.black)
user_frame.pack()

user_label = ctk.CTkLabel(user_frame,
                          text="Please log in to use the application",
                          fg_color=mn.black,
                          bg_color=mn.black)
user_label.pack(side="right", padx=10)

# Body
body = ctk.CTkFrame(master,
                    fg_color=mn.black,
                    bg_color=mn.black)
body.grid(row=1, column=0, columnspan=2, sticky="nsew")

scrollbody = ctk.CTkScrollableFrame(body,
                              fg_color=mn.primary_grey    ,
                              bg_color=mn.black)
scrollbody.pack(side="right", fill="both", expand=True, padx=(0,6))

nav_frame = ctk.CTkFrame(body,
                         fg_color=mn.black,
                         bg_color=mn.black,
                         width=156)
nav_frame.pack(side="left", fill="y")


menu_frame = ctk.CTkFrame(nav_frame,
                          fg_color=mn.black,
                          bg_color=mn.black,
                          width=nav_frame._current_width)
menu_frame.pack(side="top")

nav_logout_frame = ctk.CTkFrame(nav_frame,
                                fg_color=mn.black,
                                bg_color=mn.black,
                                width=nav_frame._current_width)
nav_logout_frame.pack(side="bottom")

main_frame = ctk.CTkFrame(scrollbody,
                          fg_color=mn.primary_grey,
                          bg_color=mn.primary_grey)
main_frame.custom_name = "main"
main_frame.pack(fill="both", expand=True)
master.grid_columnconfigure(0, weight=1)
master.grid_columnconfigure(1, weight=0)

# Body functions
def nav_setup(frame):
    if mn.user.username != None:
        home_btn = ctk.CTkButton(menu_frame,
                                text="Home",
                                fg_color=mn.secondary_grey,
                                command=lambda: home_page(main_frame))
        home_btn.grid(row=0, column=0, padx=(0, 0), pady=(0, 5))

        user_btn = ctk.CTkButton(menu_frame,
                                text="User",
                                fg_color=mn.secondary_grey,
                                command=lambda: user_page(main_frame))
        user_btn.grid(row=1, column=0, padx=(0, 0), pady=(0, 5))

        database_btn = ctk.CTkButton(menu_frame,
                                    text="Database",
                                    fg_color=mn.secondary_grey,
                                    command=lambda: database_page(main_frame))
        database_btn.grid(row=2, column=0, padx=(0, 0), pady=(0, 5))

        beregn_btn = ctk.CTkButton(menu_frame,
                                text="Beregn",
                                fg_color=mn.secondary_grey,
                                command=lambda: beregn_page(main_frame))
        beregn_btn.grid(row=3, column=0, padx=(0, 0), pady=(0, 5))

        settings_btn = ctk.CTkButton(menu_frame,
                                    text="Settings",
                                    fg_color=mn.secondary_grey,
                                    command=lambda: settings_page(main_frame))
        settings_btn.grid(row=4, column=0, padx=(0, 0), pady=(0, 5))

        logs_btn = ctk.CTkButton(menu_frame,
                                text="Logs",
                                fg_color=mn.secondary_grey,
                                command=lambda: logs_page(main_frame))
        logs_btn.grid(row=5, column=0, padx=(0, 0), pady=(0, 5))

        if mn.user.admin == True:
            
            splitter = ctk.CTkFrame(menu_frame,
                                      fg_color=mn.black,
                                      bg_color=mn.black,
                                      width = 0,
                                      height = 20)
            splitter.grid(row=6, column=0)

            admin_btn1 = ctk.CTkButton(menu_frame,
                                    text="Admin settings",
                                    fg_color=mn.green_color,
                                    command=lambda: admin_settings_page(main_frame))
            admin_btn1.grid(row=7, column=0, padx=(0, 0), pady=(0, 5))

            admin_btn2 = ctk.CTkButton(menu_frame,
                                    text="Admin2",
                                    fg_color=mn.green_color)
            admin_btn2.grid(row=8, column=0, padx=(0, 0), pady=(0, 5))

def login_page(frame):
    mn.clear_frame(frame)
    login_frame = ctk.CTkFrame(frame,
                               border_width=1,
                               fg_color=mn.black)
    login_frame.pack(expand=True, pady=(master._current_height/3, 0))

    username_label = ctk.CTkLabel(login_frame,
                                  text="Username")
    username_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)

    username_entry = ctk.CTkEntry(login_frame)
    username_entry.grid(row=0, column=1, sticky="w", padx=5, pady=5)

    password_label = ctk.CTkLabel(login_frame,
                                  text="Password",)
    password_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)

    password_entry = ctk.CTkEntry(login_frame,
                                  show="*")
    password_entry.grid(row=1, column=1, sticky="w", padx=5, pady=5)

    login_button = ctk.CTkButton(login_frame,
                                 fg_color=mn.green_color,
                                 text="Login", 
                                 border_width=1,
                                 border_color=mn.black,
                                 command=lambda: login(username_entry.get(), username_entry, password_entry))
    login_button.grid(row=2, column=0, columnspan=2, sticky="ew", padx=3, pady=3)

    frame.after(150, lambda: username_entry.focus())
    username_entry.bind('<Return>', lambda event: password_entry.focus())
    password_entry.bind('<Return>', lambda event: login(username_entry.get(), username_entry, password_entry))

    password_entry.bind('<Up>', lambda event: username_entry.focus())
    username_entry.bind('<Down>', lambda event: password_entry.focus())

    mn.current_page = "Login"
    master.title(f"{mn.app_title} - {mn.current_page}")

    return login_frame

def home_page(frame):
    if mn.current_page == "Home":
        print("Already on home page")
    elif not user.username == None:
        mn.clear_frame(frame)

        home_frame = ctk.CTkFrame(frame, fg_color=mn.background_grey)
        home_frame.pack(pady=5)

        btn_list = []

        user_btn = ctk.CTkButton(home_frame,
                                 text="User",
                                 height=100,
                                 fg_color=mn.secondary_grey,
                                 command=lambda: user_page(frame),
                                 border_width=1,
                                 border_color=mn.black)
        btn_list.append(user_btn)

        database_btn = ctk.CTkButton(home_frame,
                                     text="Database",
                                     height=100,
                                     fg_color=mn.secondary_grey,
                                     command=lambda: database_page(frame),
                                 border_width=1,
                                 border_color=mn.black)
        btn_list.append(database_btn)

        beregn_btn = ctk.CTkButton(home_frame,
                                   text="Beregn",
                                   height=100,
                                   fg_color=mn.secondary_grey,
                                   command=lambda: beregn_page(frame),
                                 border_width=1,
                                 border_color=mn.black)
        btn_list.append(beregn_btn)

        settings_btn = ctk.CTkButton(home_frame,
                                     text="Settings",
                                     height=100,
                                     fg_color=mn.secondary_grey,
                                     command=lambda: settings_page(frame),
                                 border_width=1,
                                 border_color=mn.black)
        btn_list.append(settings_btn)

        logs_btn = ctk.CTkButton(home_frame,
                                    text="Logs",
                                    height=100,
                                    fg_color=mn.secondary_grey,
                                    command=lambda: logs_page(frame),
                                 border_width=1,
                                 border_color=mn.black)
        btn_list.append(logs_btn)

        if user.admin == True:
            admin_btn1 = ctk.CTkButton(home_frame,
                                      text="Admin settings",
                                      height=100,
                                      fg_color=mn.green_color,
                                      command=lambda: admin_settings_page(frame),
                                 border_width=1,
                                 border_color=mn.black)
            btn_list.append(admin_btn1)

            admin_btn2 = ctk.CTkButton(home_frame,
                                      text="Admin2",
                                        height=100,
                                      fg_color=mn.green_color,
                                 border_width=1,
                                 border_color=mn.black)
            btn_list.append(admin_btn2)
        
        i = 0
        j = 0
        while True:
            btn_list[i].grid(row=j, column=(i-(3*j)), padx=3, pady=(0, 6))
            if ((i+1) / 3).is_integer():
                j+=1
            i+=1
            if btn_list.__len__() == i:
                break


        mn.current_page = "Home"
        master.title(f"{mn.app_title} - {mn.current_page}")
    else:
        print("Please log in first")
    # resize("")

def settings_page(frame):
        mn.clear_frame(frame)
        frame_configure(frame)
        button_gen(frame, udb.get_labels())
        settings_frame = ctk.CTkFrame(frame,
                                    border_width=1)
        settings_frame.pack()
        mn.current_page = "Settings"
        master.title(f"{mn.app_title} - {mn.current_page}")

def database_page(frame):
        mn.clear_frame(frame)
        frame_configure(frame)

        minor_db_frame1 = ctk.CTkFrame(frame,
                                                 bg_color=mn.primary_grey,
                                                 fg_color=mn.primary_grey, 
                                                 width=frame._current_width,
                                                 height=400,
                                                 border_width=1)
        
        minor_db_header1 = ctk.CTkLabel(minor_db_frame1,
                                        text="Workers",
                                        font=("Arial", 18),
                                        text_color=mn.black)
        minor_db_header1.pack(pady=2)
        minor_db_frame1.pack(padx=5, pady=5)

        minor_db_frame2 = ctk.CTkFrame(frame,
                                       bg_color=mn.primary_grey,
                                       fg_color=mn.primary_grey,
                                       width=frame._current_width,
                                       border_width=1)
        minor_db_header2 = ctk.CTkLabel(minor_db_frame2,
                                        text="Material specifications",
                                        font=("Arial", 18),
                                        text_color=mn.black)
        minor_db_header2.pack(pady=2)
        minor_db_frame2.pack(padx=5, pady=5)

        workers_table = ts.show_table(minor_db_frame1, ntdb.sql_select_workers_data())
        material_table = ts.show_table(minor_db_frame2, ntdb.sql_select_material_specifications_data())

        workers_table.pack(expand=True)
        material_table.pack(expand=True)

        

        mn.current_page = "Database"
        master.title(f"{mn.app_title} - {mn.current_page}")

def user_page(frame):
    mn.clear_frame(frame)
    frame_configure(frame)
    frame.configure(border_width=0)

    first_frame = ctk.CTkFrame(frame, width=0, height=0, fg_color=mn.primary_grey)
    first_frame.pack(pady=(5, 0))
        # Insert a new user for admins
    if user.admin == True:
        testframe = ctk.CTkFrame(first_frame,
                                     border_width=1,
                                     fg_color=mn.secondary_grey)
        testframe.pack(fill="both")
        label = ctk.CTkLabel(testframe,
                                text="Insert new user",
                                font=("Arial", 18),
                                fg_color=mn.secondary_grey)
        label.pack(fill="both", padx=5, pady=5)
        new_user_frame = ctk.CTkFrame(first_frame,
                                          border_width=1,
                                          fg_color=mn.secondary_grey)
            
        new_user_frame.pack(fill="both")
            
            

        new_user_username_label = ctk.CTkLabel(new_user_frame,
                                                   text="Username")
        new_user_username_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        new_user_username_entry = ctk.CTkEntry(new_user_frame)
        new_user_username_entry.grid(row=0, column=1, sticky="w", padx=5, pady=5)
        new_user_password_label = ctk.CTkLabel(new_user_frame,
                                                   text="Password")
        new_user_password_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        new_user_password_entry = ctk.CTkEntry(new_user_frame)
        new_user_password_entry.grid(row=1, column=1, sticky="w", padx=5, pady=5)
        new_user_admin_label = ctk.CTkLabel(new_user_frame,
                                                text="Admin")
        new_user_admin_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)
        new_user_admin_entry = ctk.CTkCheckBox(new_user_frame,
                                                   text="")
        new_user_admin_entry.grid(row=2, column=1, sticky="w", padx=5, pady=5)
        new_user_button = ctk.CTkButton(new_user_frame,
                                           text="Insert user",
                                           fg_color=mn.green_color,
                                           border_width=1,
                                           border_color=mn.black,
                                           command=lambda: insert_user(first_frame, new_user_username_entry, new_user_password_entry, new_user_admin_entry))
        new_user_button.grid(row=3, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

    second_frame = ctk.CTkFrame(frame, width=0, height=0, fg_color=mn.primary_grey)
    second_frame.pack(pady=5)

    user_creation_table = ts.show_table(second_frame, ldb.select_user_creation_logs())
    user_creation_table.pack(expand=True, padx=5, pady=5)

    mn.current_page = "User"
    master.title(f"{mn.app_title} - {mn.current_page}")

def beregn_page(frame):
    mn.clear_frame(frame)
    frame_configure(frame)

    # Get data for the comboboxes/selections
    material_specs = ntdb.sql_select_material_specifications_data()

    input_header_frame = ctk.CTkFrame(frame, fg_color=mn.secondary_grey, bg_color=mn.primary_grey, border_width=1)
    input_header_frame.pack(pady=(5, 0))

    # Create base frame for page
    beregn_frame = ctk.CTkFrame(frame, fg_color=mn.secondary_grey, bg_color=mn.primary_grey, border_width=1)
    beregn_frame.pack()
    # Create input frame for calculation
    input_frame = ctk.CTkFrame(beregn_frame, fg_color=mn.secondary_grey)
    input_frame.pack(padx=2, pady=2)

    # Create a footer frame for calculation
    output_frame = ctk.CTkFrame(beregn_frame, fg_color=mn.secondary_grey)
    output_frame.pack(pady=(0, 5))

    ### Header for input frame
    header_label = ctk.CTkLabel(input_header_frame,
                                text="Calculate material cost",
                                font=("Arial", 18),
                                fg_color=mn.secondary_grey,
                                bg_color=mn.secondary_grey,
                                corner_radius=5)
    header_label.pack(padx=2, pady=2)


    
    ### GUI for input frame
    printtype_label = ctk.CTkLabel(input_frame,
                                text="Print type")
    printtype_label.grid(row=0, column=0, padx=5, pady=5)
    
    printtype_combo = ttk.Combobox(input_frame,
                                   values=[i for i in material_specs["printType"].unique()],
                                    width=20,
                                    state="readonly")
    printtype_combo.grid(row=0, column=1, padx=5, pady=5, sticky="w")
    
    def printtype_callback(*args):
        # Empty dataframe
        df = pd.DataFrame()
        
        calculate_button.configure(fg_color=mn.green_color)

        # Get the process by the selected printtype
        df = ntdb.sql_select_process_by_printtype(printtype_combo.get())
        process_combo["values"] = [i for i in df["process"].unique()]
        process_combo.current(0)

        # Get the machine by the selected process
        df = ntdb.sql_select_machine_by_process(process_combo.get())
        machine_combo["values"] = [i for i in df["machine"].unique()]
        machine_combo.current(0)

        # Get the material by the selected machine
        df = ntdb.sql_select_material_by_machine(machine_combo.get())
        material_combo["values"] = [i for i in df["materialId"].unique()]
        material_combo.current(0)

    printtype_combo.bind("<<ComboboxSelected>>", printtype_callback)

    process_label = ctk.CTkLabel(input_frame,
                                text="Process")
    process_label.grid(row=1, column=0, padx=5, pady=5)

    process_combo = ttk.Combobox(input_frame,
                                values=[i for i in material_specs["process"].unique()],
                                width=20,
                                state="readonly")
    process_combo.grid(row=1, column=1, padx=5, pady=5)
    
    def process_callback(*args):
        # Empty dataframe
        df = pd.DataFrame()
        
        calculate_button.configure(fg_color=mn.green_color)

        # Get the machine by the selected process
        df = ntdb.sql_select_machine_by_process(process_combo.get())
        machine_combo["values"] = [i for i in df["machine"].unique()]
        machine_combo.current(0)

        # Get the material by the selected machine
        df = ntdb.sql_select_material_by_machine(machine_combo.get())
        material_combo["values"] = [i for i in df["materialId"].unique()]
        material_combo.current(0)
    
    process_combo.bind("<<ComboboxSelected>>", process_callback)

    machine_label = ctk.CTkLabel(input_frame,
                                text="Machine *")
    machine_label.grid(row=2, column=0, padx=5, pady=5)

    machine_combo = ttk.Combobox(input_frame,
                                values=[i for i in material_specs["machine"].unique()],
                                width=20,
                                state="readonly")
    machine_combo.grid(row=2, column=1, padx=5, pady=5)
    
    def machine_callback(*args):
        # Empty dataframe
        df = pd.DataFrame()

        calculate_button.configure(fg_color=mn.green_color)

        # Get the material by the selected machine
        df = ntdb.sql_select_material_by_machine(machine_combo.get())
        material_combo["values"] = [i for i in df["materialId"].unique()]
        material_combo.current(0)

    machine_combo.bind("<<ComboboxSelected>>", machine_callback)

    material_label = ctk.CTkLabel(input_frame,
                                text="Material")
    material_label.grid(row=3, column=0, padx=5, pady=5)

    material_combo = ttk.Combobox(input_frame,
                                width=20,
                                state="readonly",
                                values=["Select a machine"])
    material_combo.grid(row=3, column=1, padx=5, pady=5)

    # Mass or volume
    mass_volume_label = ctk.CTkLabel(input_frame,
                                    text="Mass or volume")
    mass_volume_label.grid(row=4, column=0, padx=5, pady=5)

    mass_volume_combo = ttk.Combobox(input_frame,
                                    values=["Mass", "Volume"],
                                    width=20,
                                    state="readonly")
    mass_volume_combo.current(0)
    mass_volume_combo.grid(row=4, column=1, padx=5, pady=5)

    def mass_volume_callback(*args):
        if mass_volume_combo.get() == "Mass":
            mass_volume_amount_unit_label.configure(text="kg")
        else:
            mass_volume_amount_unit_label.configure(text="L")
    
    mass_volume_combo.bind("<<ComboboxSelected>>", mass_volume_callback)

    mass_volume_amount_label = ctk.CTkLabel(input_frame,
                                            text="Material amount")
    mass_volume_amount_label.grid(row=5, column=0, padx=5, pady=5)

    mass_volume_amount_entry = ctk.CTkEntry(input_frame, width=130, height=20)
    mass_volume_amount_entry.grid(row=5, column=1, sticky="w", padx=(4,0))

    unit_label_frame = ctk.CTkFrame(input_frame, fg_color=mn.secondary_grey, bg_color=mn.secondary_grey)
    unit_label_frame.grid(row=5, column=1, padx=(mass_volume_amount_entry._current_width, 0))

    mass_volume_amount_unit_label = ctk.CTkLabel(unit_label_frame,
                                                 text="kg",
                                                 width=14)
    mass_volume_amount_unit_label.pack(side="left")

    calculate_button = ctk.CTkButton(output_frame,
                                    text="Calculate",
                                    fg_color=mn.secondary_grey, 
                                    border_width=1,
                                    border_color=mn.black,
                                    command=lambda: btn_calculate())
    calculate_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

    def btn_calculate():
        try :
            if mass_volume_amount_entry.get().replace(",", ".") == "":
                raise ValueError("Please enter a value")
            if float(mass_volume_amount_entry.get().replace(",", ".")) <= 0:
                raise ValueError("Please enter a positive number")
        except ValueError as e:
            calc_error_label.configure(text=e)
            mass_volume_amount_entry.configure(border_color="red", border_width=1)
            return
        mass_volume_amount_entry.configure(border_color="grey", border_width=0)
        # If mass or volume is selected in the mass_volume_combobox
        if mass_volume_combo.get() == "Mass":
            print_cost = dh.get_print_cost_from_mass(machine_combo.get(), material_combo.get(), "kg", mass_volume_amount_entry.get().replace(",", "."))
            calc_error_label.configure(text=f"Material cost: {print_cost:.2f} $")
            ldb.insert_raw_cost_calculation_log(machine_combo.get(), material_combo.get(), mass_volume_amount_entry.get().replace(",", "."), "kg", print_cost)
            mn.clear_frame(raw_cost_logs_frame)
            ts.show_table(raw_cost_logs_frame, ldb.select_raw_cost_calculation_logs()).pack(expand=True)
        elif mass_volume_combo.get() == "Volume":
            print_cost = dh.get_print_cost_from_volume(machine_combo.get(), material_combo.get(), "L", mass_volume_amount_entry.get().replace(",", "."))
            calc_error_label.configure(text=f"Material cost: {print_cost:.2f} $")
            ldb.insert_raw_cost_calculation_log(machine_combo.get(), material_combo.get(), mass_volume_amount_entry.get().replace(",", "."), "L", print_cost)
            mn.clear_frame(raw_cost_logs_frame)
            ts.show_table(raw_cost_logs_frame, ldb.select_raw_cost_calculation_logs()).pack(expand=True)


    calc_error_label = ctk.CTkLabel(output_frame, text="", width=header_label._current_width)
    calc_error_label.grid(row=7, column=0)

    reset_calc_button = ctk.CTkButton(output_frame,
                                    text="Reset",
                                    command=lambda: reset_calculate())
    reset_calc_button.grid(row=8, column=0)

    def reset_calculate():
        beregn_page(frame)

    
    raw_cost_logs_frame = ctk.CTkFrame(frame, fg_color=mn.primary_grey)
    raw_cost_logs_frame.pack(padx=1, pady=1)
    raw_table = ts.show_table(raw_cost_logs_frame, ldb.select_raw_cost_calculation_logs())
    raw_table.pack(expand=True)

    def on_double_click_raw_cost_log(event):
        item = raw_table.selection()[0]
        print(item)
        print("Double clicked")

    raw_table.bind("<Double-1>", on_double_click_raw_cost_log)

    header_label.configure(width=input_frame._current_width)

    mn.current_page = "Beregn"
    master.title(f"{mn.app_title} - {mn.current_page}")

def admin_settings_page(frame):
    mn.clear_frame(frame)
    frame_configure(frame)

    button_gen(frame, udb.get_labels())
    settings_frame = ctk.CTkFrame(frame, border_width=1)
    settings_frame.pack()

    mn.current_page = "Admin Settings"
    master.title(f"{mn.app_title} - {mn.current_page}")

def logs_page(frame):
    mn.clear_frame(frame)
    frame_configure(frame)

    mn.current_page = "Logs"
    master.title(f"{mn.app_title} - {mn.current_page}")

# Run body functions
nav_setup(menu_frame)
login_page(main_frame)

# Footer
footer = ctk.CTkFrame(master,
                      fg_color=mn.black,
                      bg_color=mn.black,
                      height=8,
                      width=master._current_width)
footer.custom_name = "footer"
footer.grid(row=2, column=0, columnspan=2)

# Tkinter functions

# Real functions
def login(username, username_entry, password_entry):
    check = udb.check_login(username_entry.get(), password_entry.get())
    if check[0] is True:
        btn = ctk.CTkButton(nav_logout_frame,
                    text="Logout",
                    command=lambda: logout(),
                    fg_color=mn.secondary_grey,
                    border_color="red",
                    border_width=1)
        btn.grid(row=0, column=0, padx=8)
        user.username = username
        if check[1] == 1:
            user.admin = True
            mn.user = user
            logo_label.configure(image=admin_logo)
        else:
            user.admin = False
            logo_label.configure(image=logo)
        # mn.clear_frame(main_frame)
        # main_frame.pack()
        home_page(main_frame)
        user_label.configure(text=f"Hello, {mn.user.username}")
        greet_user()
        nav_setup(menu_frame)
    else:
        print("Wrong username or password")
        username_entry
        username_entry.configure(border_color="red",
                                 border_width=1)
        password_entry.configure(border_color="red",
                                 border_width=1)

def logout():
    user.username = None
    print("Logged out")
    user_label.configure(text="Please log in to use the application")
    login_page(main_frame)
    mn.clear_frame(menu_frame)
    mn.clear_frame(nav_logout_frame)
    logo_label.configure(image=logo)
    # some_label.configure(height=(master._current_height-(header._current_height+footer._current_height+menu_frame._current_height+15)))

def insert_user(frame, username, password, admin):
    testlabel = ctk.CTkLabel(frame,
                             bg_color=mn.black,)
    testlabel.pack(fill="both")
    try:
        udb.insert_user(username.get(), password.get(), admin.get())
        testlabel.configure(text="User inserted")
        username.delete(0, "end")
        password.delete(0, "end")
        username.configure(border_color=mn.secondary_grey)
        user_page(main_frame)

    except NameError as e:
        testlabel.configure(text=f"User already exists")
        username.configure(border_color="red")
        print(e)
    except Exception as e:
        testlabel.configure(text=f"User not inserted")
        print(e)

def frame_configure(frame):
    frame.configure(border_width=0,
                    width=400,
                    fg_color="#d9d9d9",)

# Big reset
def restart_dbs():
    ntdb.restart_tables_NextTech_db()
    udb.restart_tables_users_db()
    ldb.restart_logs()

# restart_dbs()

list_of_resizes = []
def resize(event):
    scrollbody.configure(height=master._current_height-(header._current_height+footer._current_height+15))
    list_of_resizes.append("")
    print(list_of_resizes.__len__())

body.bind("<Configure>", resize)

# Run main loop
master.mainloop()