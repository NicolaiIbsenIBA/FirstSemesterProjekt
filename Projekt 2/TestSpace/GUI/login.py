import my_queries as mq
from tkinter import *
import customtkinter as ctk

def login_window():
    # Login function
    def login(username, password):
            global my_bool
            if username == 'admin' and password == 'admin':
                print('Login successful')
                my_bool = True
                login_root.destroy()
            else:
                print('Login failed')
                username_entry.configure(border_color='red')
                password_entry.configure(border_color='red')
                my_bool = False
    
    # Login window
    login_root = ctk.CTk()
    login_root.geometry('200x200')
    login_root.title('Login')

    username_entry = ctk.CTkEntry(login_root,
                                placeholder_text='Username',)
    password_entry = ctk.CTkEntry(login_root,
                                placeholder_text='Password',
                                show='*')
    
    login_button = ctk.CTkButton(login_root,
                                text='Login',
                                command=lambda: login(username_entry.get(), password_entry.get()))
    
    username_entry.pack()
    password_entry.pack()
    login_button.pack()

    # Tkinter functions
    login_root.after(50, lambda: username_entry.focus())

    username_entry.bind('<Return>', lambda event: password_entry.focus())
    password_entry.bind('<Return>', lambda event: login(username_entry.get(), password_entry.get()))

    password_entry.bind('<Up>', lambda event: username_entry.focus())
    username_entry.bind('<Down>', lambda event: password_entry.focus())
    

    login_root.mainloop()