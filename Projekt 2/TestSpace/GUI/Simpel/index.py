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

def show_table(frame, liste):
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

# Real functions
def login(username, username_entry, password_entry):
    check = udb.check_login(username_entry.get(), password_entry.get())
    if check[0] is True:
        btn = ctk.CTkButton(footer,
                    text="Logout",
                    command=lambda: logout(),
                    fg_color=mn.secondary_grey,
                    border_color="red",
                    border_width=1)
        btn.pack(side="right")
        user.username = username
        if check[1] == 1:
            user.admin = True
            logo_label.configure(image=admin_logo)
        else:
            user.admin = False
            logo_label.configure(image=logo)
        # mn.clear_frame(main_frame)
        main_frame.pack()
        home_page(main_frame)
        greet_user()
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
    mn.clear_frame(footer)
    login_page(main_frame)
    logo_label.configure(image=logo)

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

    except NameError as e:
        testlabel.configure(text=f"User already exists")
        username.configure(border_color="red")
        print(e)
    except Exception as e:
        testlabel.configure(text=f"User not inserted")
        print(e)

def frame_configure(frame):
    frame.configure(border_width=1,
                    width=400)

# Main window
master = ctk.CTk()
master.geometry("500x600")
master.iconbitmap(mn.ico)
master.title("NexText CALC")

# Header
header = ctk.CTkFrame(master,
                      fg_color=mn.black,
                      bg_color=mn.black,
                      height=50)
header.custom_name = "header"
header.pack(side="top", fill="both")

icon = ctk.CTkImage(light_image=Image.open(mn.home_icon), size=(50, 50))
icon_label = ctk.CTkButton(header, 
                           image=icon, 
                           command=lambda: home_page(main_frame), 
                           text="",
                           width=1,
                           bg_color=mn.black,
                           fg_color=mn.black)
icon_label.grid(row=0, column=0, sticky="w", padx=3, pady=3)

logo = ctk.CTkImage(light_image=Image.open(mn.logo), size=(200, 50))
admin_logo = ctk.CTkImage(light_image=Image.open(mn.admin_logo), size=(200, 50))
logo_label = ctk.CTkLabel(header, 
                          image=logo, 
                          text="")
logo_label.grid(row=0, column=3, sticky="ew")

dropdown = ctk.CTkComboBox(header, 
                           values=["Material Specifications", "Workers"])
dropdown.grid(row=0, column=5, sticky="e", padx=3, pady=3)

def grid_configure(header_frame):
    header_frame.grid_columnconfigure(0, weight=1)
    header_frame.grid_columnconfigure(1, weight=1)
    header_frame.grid_columnconfigure(2, weight=1)
    header_frame.grid_columnconfigure(3, weight=2)
    header_frame.grid_columnconfigure(4, weight=1)
    header_frame.grid_columnconfigure(5, weight=1)
grid_configure(header)

# Body
body = ctk.CTkScrollableFrame(master,
                              fg_color=mn.primary_grey,
                              bg_color=mn.primary_grey)
body.pack(fill="both", expand=True)

main_frame = ctk.CTkFrame(body,
                          fg_color=mn.primary_grey,
                          bg_color=mn.primary_grey,
                          width=500,)
main_frame.custom_name = "main"
main_frame.pack(padx=3, pady=3)

# Body functions
def login_page(frame):
    mn.clear_frame(frame)
    login_frame = ctk.CTkFrame(frame,
                               border_width=1,
                               fg_color=mn.black)
    login_frame.pack()

    username_label = ctk.CTkLabel(login_frame,
                                  text="Username")
    username_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)

    username_entry = ctk.CTkEntry(login_frame)
    username_entry.grid(row=0, column=1, sticky="w", padx=5, pady=5)

    password_label = ctk.CTkLabel(login_frame,
                                  text="Password")
    password_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)

    password_entry = ctk.CTkEntry(login_frame)
    password_entry.grid(row=1, column=1, sticky="w", padx=5, pady=5)

    login_button = ctk.CTkButton(login_frame,
                                 fg_color=mn.green_color,
                                 text="Login",
                                 command=lambda: login(username_entry.get(), username_entry, password_entry))
    login_button.grid(row=2, column=0, columnspan=2, sticky="ew", padx=3, pady=3)

    frame.after(50, lambda: username_entry.focus())
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
        frame_configure(frame)

        user_btn = ctk.CTkButton(frame,
                                 text="User",
                            height=100,
                            fg_color=mn.secondary_grey,
                                 command=lambda: user_page(frame))
        user_btn.grid(row=0, column=0, padx=5, pady=5)


        database_btn = ctk.CTkButton(frame,
                                     text="Database",
                            height=100,
                            fg_color=mn.secondary_grey,
                                     command=lambda: database_page(frame))
        database_btn.grid(row=0, column=1, padx=5, pady=5)

        settings_btn = ctk.CTkButton(frame,
                            text="Settings",
                            height=100,
                            fg_color=mn.secondary_grey,
                            command=lambda: settings_page(frame))
        settings_btn.grid(row=0, column=2, padx=5, pady=5)

        if user.admin == True:
            admin_btn1 = ctk.CTkButton(frame,
                                      text="Admin1",
                            height=100,
                                      fg_color=mn.green_color)
            admin_btn1.grid(row=1, column=0, padx=5, pady=5)

            admin_btn2 = ctk.CTkButton(frame,
                                      text="Admin2",
                            height=100,
                                      fg_color=mn.green_color)
            admin_btn2.grid(row=1, column=1, padx=5, pady=5)

        mn.current_page = "Home"
        master.title(f"{mn.app_title} - {mn.current_page}")
    else:
        print("Please log in first")

def settings_page(frame):
    if not user.username == "":
        mn.clear_frame(frame)
        frame_configure(frame)
        button_gen(frame, udb.get_labels())
        settings_frame = ctk.CTkFrame(frame,
                                    border_width=1)
        settings_frame.pack()
        mn.current_page = "Settings"
        master.title(f"{mn.app_title} - {mn.current_page}")

def database_page(frame):
    if not user.username == "":
        mn.clear_frame(frame)
        frame_configure(frame)

        minor_db_frame1 = ctk.CTkScrollableFrame(frame,
                                                 bg_color=mn.primary_grey,
                                                 fg_color=mn.primary_grey)

        minor_db_frame2 = ctk.CTkFrame(frame,
                                       bg_color=mn.primary_grey,
                                       fg_color=mn.primary_grey)

        minor_db_frame1.pack(padx = 3, pady=3, fill="both")
        minor_db_frame2.pack(padx = 3, pady=3, fill="both")

        confirm_btn = ctk.CTkButton(frame,
                                    text="Confirm",
                                    fg_color=mn.green_color,
                                    command=lambda: dh.confirm_changed_workers())
        confirm_btn.pack(side="bottom", fill="both")

        if mn.dictionary["material_specifications_data"] is None:
            mn.dictionary["material_specifications_data"] = ntdb.sql_select_material_specifications_data()
        if mn.dictionary["workers_data"] is None:
            mn.dictionary["workers_data"] = ntdb.sql_select_workers_data()

        show_table(minor_db_frame1, mn.dictionary["material_specifications_data"])
        show_table(minor_db_frame2, mn.dictionary["workers_data"])

        mn.current_page = "Database"
        master.title(f"{mn.app_title} - {mn.current_page}")

def user_page(frame):
    if not user.username == "":
        mn.clear_frame(frame)
        frame_configure(frame)
        frame.configure(border_width=0)
        # Insert a new user for admins
        if user.admin == True:
            testframe = ctk.CTkFrame(frame,
                                     border_width=1,
                                     fg_color=mn.secondary_grey)
            testframe.pack(fill="both")
            label = ctk.CTkLabel(testframe,
                                text="Insert new user",
                                font=("Arial", 18),
                                fg_color=mn.secondary_grey)
            label.pack(fill="both", padx=5, pady=5)
            new_user_frame = ctk.CTkFrame(frame,
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
                                           command=lambda: insert_user(frame, new_user_username_entry, new_user_password_entry, new_user_admin_entry))
            new_user_button.grid(row=3, column=0, columnspan=2, sticky="ew", padx=5, pady=5)


        mn.current_page = "User"
        master.title(f"{mn.app_title} - {mn.current_page}")

# Run body functions
login_page(main_frame)

# Footer
footer = ctk.CTkFrame(master,
                      fg_color=mn.black,
                      bg_color=mn.black,
                      height=28)
footer.custom_name = "footer"
footer.pack(side="bottom", fill="both")

# Tkinter functions

# Run main loop
master.mainloop()