import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

# Opret hovedvinduet
root = tk.Tk()
root.title("3D Print Beregner")
root.geometry("300x100")
#Ændre baggrundsfarve
root.configure(bg='#009FE3')

#opretter en etikette
label= tk.Label(root, text= "Velkommen til Nexttech!", bg='#009FE3')

def upload_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        upload_button.config(text="Fil valgt")
    else:
        upload_button.config(text="Vælg fil")



# Venstre side - Upload knap
upload_button = tk.Button(root, text="Upload 3D-fil", command=upload_file)
upload_button.grid(row=0, column=0, padx=10, pady=10, sticky="w")

# Højre side - Materialevalg
material_Label = tk.Label(root, text="Vælg materiale:")
material_Label.grid(row=0, column=1, padx=10, sticky="w")  # Ret til sticky="w"

material_options = ["PLA", "ABS", "PETG", "Nylon"]
material_var = tk.StringVar(value=material_options[0])
material_dropdown = ttk.Combobox(root, textvariable=material_var, values=material_options)  # Ret til materiale_dropdown
material_dropdown.grid(row=0, column=2, padx=10, pady=10, sticky="w")

# Højre side - Printvalg
printer_label = tk.Label(root, text="Vælg printer:")
printer_label.grid(row=1, column=1, padx=10, sticky="w")

printer_options = ["Printer FDM", "Printer SLA", "Printer MK4S"]
printer_var = tk.StringVar(value=printer_options[0])
printer_dropdown = ttk.Combobox(root, textvariable=printer_var, values=printer_options)  # Ret til printer_dropdown
printer_dropdown.grid(row=1, column=2, padx=10, pady=10, sticky="w")

# Start tkinter loop
root.mainloop()