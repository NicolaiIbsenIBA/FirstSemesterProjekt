import customtkinter as c
from PIL import Image
import Simpel.my_names as mn
import structure as struct

# If not logged in say "Hello Guest", else say "Hello {username}"
def greet_user(master):
    if mn.user.username == "":
        print("Hello guest")
    else:
        print(f"Hello {mn.user.username}")
        mn.clear_frame(header_frame)
        header_frame(master)

def header_frame(master):
    header_frame = c.CTkFrame(master, fg_color=mn.black, bg_color=mn.black)
    header_frame.pack(fill="both")        

    icon = c.CTkImage(light_image=Image.open("Assets/IBA_icon.png"), size=(50, 50))
    icon_label = c.CTkButton(header_frame, 
                            image=icon, 
                                 command=lambda: greet_user(master), 
                                 text="",
                                 width=1,
                                 bg_color=mn.black,
                                 fg_color=mn.black)

    logo = c.CTkImage(light_image=Image.open("Assets/logo.png"), size=(200, 50))
    logo_label = c.CTkLabel(header_frame, image=logo, text="")

    dropdown = c.CTkComboBox(header_frame, values=["Material Specifications", "Workers"])

    header_frame.grid_columnconfigure(0, weight=1)
    header_frame.grid_columnconfigure(1, weight=1)
    header_frame.grid_columnconfigure(2, weight=2)
    header_frame.grid_columnconfigure(3, weight=0)
    header_frame.grid_columnconfigure(4, weight=1)

    icon_label.grid(row=0, column=0, sticky="w", padx=3, pady=3)
    logo_label.grid(row=0, column=2, sticky="ew")
    dropdown.grid(row=0, column=4, sticky="e", padx=3, pady=3)

    return header_frame

def footer_frame(master):
    footer_frame = c.CTkFrame(master, 
                                fg_color=mn.black, 
                                bg_color=mn.primary_grey,
                                background_corner_colors=[mn.black, mn.black, mn.primary_grey, mn.primary_grey])
    footer_frame.pack(fill="both", side="bottom")

    footer_label = c.CTkLabel(footer_frame, text="© 2024 Nextech")
    footer_label.pack(expand=True, fill="both")
