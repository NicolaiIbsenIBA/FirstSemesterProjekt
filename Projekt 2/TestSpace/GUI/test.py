import tkinter as tk
import customtkinter as ctk
import pandas as pd

# Example material_specs DataFrame
material_specs = pd.DataFrame({
    'printType': ['Type1', 'Type2', 'Type3'],
    'process': ['Process1', 'Process2', 'Process3']
})

root = ctk.CTk()

frame = ctk.CTkFrame(root)
frame.pack(fill="both", expand=True)

beregn_frame = ctk.CTkFrame(frame, border_width=1, width=400, height=400)
beregn_frame.pack(fill="both", expand=True)

printtype_label = ctk.CTkLabel(beregn_frame, text="Print type")
printtype_label.grid(row=0, column=0, padx=5, pady=5)

def on_printtype_selected(*args):
    selected_value = printtype_var.get()
    print(f"Print type selected: {selected_value}")

printtype_var = tk.StringVar()
printtype_var.set(material_specs["printType"].unique()[0])  # Set default value

printtype_var.trace_add("write", on_printtype_selected)

printtype_combobox = tk.OptionMenu(beregn_frame, printtype_var, *material_specs["printType"].unique())
printtype_combobox.config(width=20)
printtype_combobox.grid(row=0, column=1, padx=5, pady=5)

process_label = ctk.CTkLabel(beregn_frame, text="Process")
process_label.grid(row=1, column=0, padx=5, pady=5)

root.mainloop()