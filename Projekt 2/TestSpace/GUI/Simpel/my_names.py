import classes as cl
import pandas as pd

labelgen = pd.DataFrame ({
            'Settings': ['Material Specifications', 'Workers', 'Machines', 'Products', 'Orders', 'Settings', 'Settings', 'Settings', 'Settings', 'Settings', 'Settings', 'Settings'],
})

# Database name and tables names
name_of_database = 'nextTech.db'
material_specifications_table = 'materialSpecifications'
material_columns = ['Materialid', 'Printtype', 'Machine', 'Process', 'Cost', 'Unit', 'Density']
workers_table = 'workers'
workers_columns = ['Process', 'Jobtitle', 'Salary']

# Name of app
app_title = "NextTech CALC"

# Assets
logo = "Assets/logo.png"
admin_logo = "Assets/logo_admin.png"
home_icon = "Assets/IBA_icon.png"
ico = "Assets/IBA_icon_ico.ico"

# Colors
light_color = "#f4f4f4"
blue_color = "#009fe3"
green_color = "#6da924"
primary_grey = "#d9d9d9"
secondary_grey = "#565b5e"
background_grey  = "#d9d9d9"
black = "#000000"

# Global variables
global user
user = cl.Credentials("", "", False) 
global current_page
current_page = ""
global dictionary
dictionary = {
    "material_specifications_data": None,
    "workers_data": None,
}


def clear_frame(frame):
    frame_name = getattr(frame, "custom_name", "Unnamed Frame")
    try:
        print(f"Clearing frame '{frame_name}'")
    except:
        print("Clearing frame")
    for widget in frame.winfo_children():
        widget.destroy()
