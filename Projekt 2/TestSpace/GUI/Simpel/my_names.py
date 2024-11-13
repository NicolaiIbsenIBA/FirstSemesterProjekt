import classes as cl
import pandas as pd

labelgen = pd.DataFrame ({
            'Settings': ['Material Specifications', 'Workers', 'Machines', 'Products', 'Orders', 'Settings', 'Settings', 'Settings', 'Settings', 'Settings', 'Settings', 'Settings'],
})

# Database name and tables names
name_of_database = 'NEXTTECH_3D_PRINTING'
material_specifications_table = 'MACHINE'
workers_table = 'WORKERS'

# Assets
logo = "Assets/logo.png"
home_icon = "Assets/IBA_icon.png"
ico = "Assets/IBA_icon_ico.ico"

# Colors
light_color = "#f4f4f4"
blue_color = "#009fe3"
green_color = "#76b82a"
primary_grey = "#d9d9d9"
secondary_grey = "#2d2d2d"
black = "#000000"

global user
user = cl.Credentials("", "", False) 

def clear_frame(frame):
    print("Clearing frame")
    for widget in frame.winfo_children():
        widget.destroy()