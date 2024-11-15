import my_queries as mq
from tkinter import *
import customtkinter as ctk
import home as h
import classes as cl
import my_names as mn

def clear_frame(frame):
    print("Clearing frame")
    for widget in frame.winfo_children():
        widget.destroy()

def login_content(master):
    # Login function
    my_frame = ctk.CTkFrame(master,
                            fg_color='#009fe3')
    my_frame.pack()

    username_label = ctk.CTkLabel(my_frame, text='Username')
    username_entry = ctk.CTkEntry(my_frame,
                                  placeholder_text='Username',)
    password_label = ctk.CTkLabel(my_frame, text='Password')
    password_entry = ctk.CTkEntry(my_frame,
                                  placeholder_text='Password',
                                  show='*',
                                  width=100)
    
    login_button = ctk.CTkButton(my_frame,
                                 text='Login',
                                 command=lambda: login(master, username_entry.get(), password_entry.get(), username_entry, password_entry))
    
    show_password_btn = ctk.CTkButton(my_frame,
                                      text='*',
                                      command=show_password(password_entry),
                                      width=20)

    my_frame.pack(expand=True)
    username_label.grid(row=0, column=0)
    username_entry.grid(row=1, column=0)
    password_label.grid(row=2, column=0)
    password_entry.grid(row=3, column=0, sticky="ew")
    show_password_btn.grid(row=3, column=1)
    login_button.grid(row=4, column=0)

    # Tkinter functions
    master.after(50, lambda: username_entry.focus())

    username_entry.bind('<Return>', lambda event: password_entry.focus())
    password_entry.bind('<Return>', lambda event: login(master, username_entry.get(), password_entry.get(), username_entry, password_entry))

    password_entry.bind('<Up>', lambda event: username_entry.focus())
    username_entry.bind('<Down>', lambda event: password_entry.focus())

def login(master, username, password, username_entry, password_entry):
    if username == 'admin' and password == 'admin':
        print('Login successful')
        clear_frame(master)
        h.homepage_content(master)
        mn.user = cl.Credentials(username, password, True)
    else:
        print('Login failed')
        username_entry.configure(border_color='red')
        password_entry.configure(border_color='red')

    # Show password function
def show_password(password_entry):
    if password_entry.cget('show') == '':
        password_entry.configure(show='*')
    else:
        password_entry.configure(show='')