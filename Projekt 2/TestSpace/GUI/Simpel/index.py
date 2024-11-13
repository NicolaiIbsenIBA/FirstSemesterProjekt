from tkinter import *
import customtkinter as ctk
import classes as cl
import my_names as mn
from PIL import Image
import db_code as db
import time

# Declare variables
user = cl.Credentials("", "", False)

# Functions
def greet_user():
    if user.username == "":
        print("Hello guest")
    else:
        print(f"Hello {user.username}")

def label_gen(labels, frame):
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

# Main window
master = ctk.CTk()
master.geometry("500x600")

# Header
header = ctk.CTkFrame(master,
                      fg_color=mn.black,
                      bg_color=mn.black,
                      height=50)
header.pack(side="top", fill="both")

icon = ctk.CTkImage(light_image=Image.open(mn.home_icon), size=(50, 50))
icon_label = ctk.CTkButton(header, 
                           image=icon, 
                           command=lambda: home_content(main_frame), 
                           text="",
                           width=1,
                           bg_color=mn.black,
                           fg_color=mn.black)
icon_label.grid(row=0, column=0, sticky="w", padx=3, pady=3)

logo = ctk.CTkImage(light_image=Image.open(mn.logo), size=(200, 50))
logo_label = ctk.CTkLabel(header, 
                          image=logo, 
                          text="")
logo_label.grid(row=0, column=3, sticky="ew")

dropdown = ctk.CTkComboBox(header, 
                           values=["Material Specifications", "Workers"])
dropdown.grid(row=0, column=5, sticky="e", padx=3, pady=3)

def grid_configure():
    header.grid_columnconfigure(0, weight=1)
    header.grid_columnconfigure(1, weight=1)
    header.grid_columnconfigure(2, weight=1)
    header.grid_columnconfigure(3, weight=2)
    header.grid_columnconfigure(4, weight=1)
    header.grid_columnconfigure(5, weight=1)
grid_configure()

# Body
body = ctk.CTkScrollableFrame(master,
                              fg_color=mn.primary_grey,
                              bg_color=mn.primary_grey)
body.pack(fill="both", expand=True)

main_frame = ctk.CTkFrame(body,
                          fg_color=mn.primary_grey,
                          bg_color=mn.primary_grey,
                          width=500)
main_frame.pack()

# Body functions
def login_content(frame):
    login_frame = ctk.CTkFrame(frame,
                               border_width=1)
    login_frame.pack()

    username_label = ctk.CTkLabel(login_frame,
                                  text="Username")
    username_label.grid(row=0, column=0, sticky="w", padx=3, pady=3)

    username_entry = ctk.CTkEntry(login_frame)
    username_entry.grid(row=0, column=1, sticky="w", padx=3, pady=3)

    password_label = ctk.CTkLabel(login_frame,
                                  text="Password")
    password_label.grid(row=1, column=0, sticky="w", padx=3, pady=3)

    password_entry = ctk.CTkEntry(login_frame)
    password_entry.grid(row=1, column=1, sticky="w", padx=3, pady=3)

    login_button = ctk.CTkButton(login_frame,
                                 text="Login",
                                 command=lambda: login(username_entry.get(), password_entry.get(), username_entry, password_entry))
    login_button.grid(row=2, column=0, columnspan=2, sticky="ew", padx=3, pady=3)

    frame.after(50, lambda: username_entry.focus())
    username_entry.bind('<Return>', lambda event: password_entry.focus())
    password_entry.bind('<Return>', lambda event: login(username_entry.get(), password_entry.get(), username_entry, password_entry))

    password_entry.bind('<Up>', lambda event: username_entry.focus())
    username_entry.bind('<Down>', lambda event: password_entry.focus())

    return login_frame

def login(username, password, username_entry, password_entry):
    if db.check_login(username, password):
        print("Logged in")
        user.username = username
        mn.clear_frame(main_frame)
        main_frame.pack()
        home_content(main_frame)
    else:
        print("Wrong username or password")
        username_entry.configure(border_color="red",
                                 border_width=1)
        password_entry.configure(border_color="red",
                                 border_width=1)

def home_content(frame):
    if not user.username == "":
        print(f"Welcome {user.username}")
        mn.clear_frame(frame)
        label_gen(db.get_labels(), frame)
        home_frame = ctk.CTkFrame(frame,
                                border_width=1)
        home_frame.pack()
    else:
        mn.clear_frame(frame)
        login_content(frame)
        print("Please log in first")

# Run body functions
login_content(main_frame)

# Footer
footer = ctk.CTkFrame(master,
                      fg_color=mn.black,
                      bg_color=mn.black,
                      height=20)
footer.pack(side="bottom", fill="both")

btn = ctk.CTkButton(footer,
                    command=lambda: mn.clear_frame(main_frame),)
btn.pack()

# Tkinter functions

# Run main loop
master.mainloop()