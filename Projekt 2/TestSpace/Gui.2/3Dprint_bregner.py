import tkinter as tk
from tkinter import ttk

# Funktion til at beregne prisen
def beregn_pris():
    try:
        # Hent værdier fra inputfelterne
        materiale = materiale_var.get()  # Rettet variabelnavn
        vægt = float(vægt_var.get())    # Tilføjet parenteser efter get()
        printtid = float(printtid_var.get())  # Tilføjet parenteser
        lagtykkelse = lagtykkelse_var.get()  # Rettet navn og fjernet ulovlig syntax

        # Definer materialepriser pr. gram (eksempelpriser)
        materiale_priser = {
            "PLA": 0.05,
            "ABS": 0.07,
            "PETG": 0.06,
            "Nylon": 0.10
        }

        # Beregn pris
        materiale_pris = materiale_priser.get(materiale, 0)
        pris = vægt * materiale_pris + printtid * 2  # Eksempel: 2 DKK/time for maskinens drift

        # Vis resultat
        resultat_label.config(text=f"Pris: {pris:.2f} DKK")
    except ValueError:
        resultat_label.config(text="Fejl: Udfyld alle felter korrekt!")

# Funktion til at nulstille alle felter
def nulstil_felter():
    materiale_var.set("PLA")
    vægt_var.set("")
    printtid_var.set("")
    lagtykkelse_var.set("0.2mm")
    resultat_label.config(text="Pris: -")

# Hovedvindue
root = tk.Tk()
root.title("3D-print prisberegner")

# Materialevalg
tk.Label(root, text="Materiale:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
materiale_var = tk.StringVar(value="PLA")  # Rettet til StringVar
materiale_dropdown = ttk.Combobox(root, textvariable=materiale_var, values=["PLA", "ABS", "PETG", "Nylon"], state="readonly")
materiale_dropdown.grid(row=0, column=1, padx=10, pady=5)

# Vægt
tk.Label(root, text="Vægt (gram):").grid(row=1, column=0, sticky="w", padx=10, pady=5)
vægt_var = tk.StringVar()  # Tilføjet variabel
vægt_entry = tk.Entry(root, textvariable=vægt_var)  # Rettet oprettelse af Entry
vægt_entry.grid(row=1, column=1, padx=10, pady=5)

# Printtid
tk.Label(root, text="Printtid (timer):").grid(row=2, column=0, sticky="w", padx=10, pady=5)
printtid_var = tk.StringVar()
printtid_entry = tk.Entry(root, textvariable=printtid_var)  # Rettet navn og entry
printtid_entry.grid(row=2, column=1, padx=10, pady=5)

# Lagtykkelse
tk.Label(root, text="Lagtykkelse:").grid(row=3, column=0, sticky="w", padx=10, pady=5)
lagtykkelse_var = tk.StringVar(value="0.2mm")
lagtykkelse_dropdown = ttk.Combobox(root, textvariable=lagtykkelse_var, values=["0.1mm", "0.2mm", "0.3mm"], state="readonly")
lagtykkelse_dropdown.grid(row=3, column=1, padx=10, pady=5)

# Beregn-knap
beregn_knap = tk.Button(root, text="Beregn", command=beregn_pris)
beregn_knap.grid(row=4, column=0, columnspan=2, pady=10)

# Reset-knap
reset_knap = tk.Button(root, text="Nulstil", command=nulstil_felter)
reset_knap.grid(row=5, column=0, columnspan=2, pady=10)

# Resultatfelt
resultat_label = tk.Label(root, text="Pris: -", font=("Arial", 12))  # Rettet font-syntax
resultat_label.grid(row=6, column=0, columnspan=2, pady=10)

# Start GUI
root.mainloop()