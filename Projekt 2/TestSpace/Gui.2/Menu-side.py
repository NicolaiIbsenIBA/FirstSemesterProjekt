import tkinter as tk
from tkinter import messagebox

def show_message(title, message):
    messagebox.showinfo(title, message)

# Funktioner til knapperne
def project_and_guides():
    show_message("3D Design - Projects and guides", "Her kan du finde projekter og guider til 3D design.")

def print_ideas():
    show_message("3D Print Ideas", "Her er nogle ideer til 3D printing.")

def practical_print():
    show_message("Practical 3D Prints", "Her er nogle praktiske 3D prints.")

def guides_reviews():
    show_message("Guides and reviews", "Her finder du guider og anmeldelser af værktøjer.")

def tools_for_fdm():
    show_message("Tools for FDM 3D Printer", "Her er værktøjer til FDM 3D printere.")
    
def print_cost_calculator():
    show_message("Print cost calculator", "Her kan du beregne omkostningerne ved 3D printning.")

def calibration_guide():
    show_message("Calibration Guide", "Her er en guide til kalibrering af din printer.")

def cnc_category():
    show_message("CNC Category", "Her finder du information om CNC bearbejdning.")

def injection_modeling():
    show_message("Injection Modeling", "Her er information om injektionsstøbning.")

def thermoforming():
    show_message("Thermoforming", "Her er information om termoformning.")

# Opret hovedvinduet
root = tk.Tk()
root.title("3D Design Application")
root.geometry("800x200")  # Ændret størrelse for at passe til vandret layout
root.configure(bg='dimgray')  # Sætter baggrundsfarven til en carbonfarve

# Opret en ramme til knapperne
frame = tk.Frame(root, bg='dimgray')
frame.pack(pady=20)

# Opret knapper med bløde kanter og farver
btn_3d_design = tk.Button(frame, text="3D Design", command=lambda: None, bg='#76B82A', width=20, height=2, borderwidth=3, relief='groove')
btn_3d_design.grid(row=0, column=0, padx=10, pady=10)

btn_tools = tk.Button(frame, text="Tools", command=lambda: None, bg='lightgray', width=20, height=2, borderwidth=3, relief='groove')
btn_tools.grid(row=0, column=1, padx=10, pady=10)

btn_more = tk.Button(frame, text="More", command=lambda: None, bg='#009FE3', width=20, height=2, borderwidth=3, relief='groove')
btn_more.grid(row=0, column=2, padx=10, pady=10)

# Tilføj undermenuer
def open_3d_design_menu():
    design_window = tk.Toplevel(root)
    design_window.title("3D Design Menu")
    
    tk.Button(design_window, text="Projects and Guides", command=project_and_guides, 
              bg='#009FE3', width=20, height=2, borderwidth=3, relief='groove').pack(pady=5)
    tk.Button(design_window, text="3D Print Ideas", command=print_ideas, bg='#009FE3',
              width=20, height=2, borderwidth=3, relief='groove').pack(pady=5)

def open_tools_menu():
    tools_window = tk.Toplevel(root)
    tools_window.title("Tools Menu")
    
    tk.Button(tools_window, text="Guides and Reviews", command=guides_reviews,
              bg='lightgreen', width=20, height=2, borderwidth=3, relief='groove').pack(pady=5)
    tk.Button(tools_window, text="Tools for FDM 3D Printer", command=tools_for_fdm,
              bg='lightgreen', width=20, height=2, borderwidth=3, relief='groove').pack(pady=5)
    tk.Button(tools_window, text="Print Cost Calculator", command=print_cost_calculator,
              bg='lightgreen', width=20, height=2, borderwidth=3, relief='groove').pack(pady=5) 
    tk.Button(tools_window, text="Calibration Guide", command=calibration_guide,
              bg='lightgreen', width=20, height=2, borderwidth=3, relief='groove').pack(pady=5)

def open_more_menu():
    more_window = tk.Toplevel(root)
    more_window.title("More Menu")
    
    tk.Button(more_window, text="CNC Category", command=cnc_category, bg='lightgray',
              width=20, height=2, borderwidth=3, relief='groove').pack(pady=5)
    tk.Button(more_window, text="Injection Modeling", command=injection_modeling,
              bg='lightgray', width=20, height=2, borderwidth=3, relief='groove').pack(pady=5)
    tk.Button(more_window, text="Thermoforming", command=thermoforming, bg='lightgray',
              width=20, height=2, borderwidth=3, relief='groove').pack(pady=5)

# Bind knapperne til funktionerne
btn_3d_design.config(command=open_3d_design_menu)
btn_tools.config(command=open_tools_menu)
btn_more.config(command=open_more_menu)

# Start GUI'en
root.mainloop()