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

    # Show password function
    def show_password():
        if password_entry.cget('show') == '':
            password_entry.configure(show='*')
        else:
            password_entry.configure(show='')
    
    # Login window
    login_root = ctk.CTk(fg_color='#009fe3')
    login_root.geometry('250x150')
    login_root.title('Login')
    login_root.resizable(False, False)
    login_root._set_appearance_mode("system")

    my_frame = ctk.CTkFrame(login_root,
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
                                 command=lambda: login(username_entry.get(), password_entry.get()))
    
    show_password_btn = ctk.CTkButton(my_frame,
                                      text='*',
                                      command=show_password,
                                      width=20)

    my_frame.pack()
    username_label.grid(row=0, column=0)
    username_entry.grid(row=1, column=0)
    password_label.grid(row=2, column=0)
    password_entry.grid(row=3, column=0, sticky="ew")
    show_password_btn.grid(row=3, column=1)
    login_button.grid(row=4, column=0)

    # Tkinter functions
    login_root.after(50, lambda: username_entry.focus())

    username_entry.bind('<Return>', lambda event: password_entry.focus())
    password_entry.bind('<Return>', lambda event: login(username_entry.get(), password_entry.get()))

    password_entry.bind('<Up>', lambda event: username_entry.focus())
    username_entry.bind('<Down>', lambda event: password_entry.focus())
    

    login_root.mainloop()