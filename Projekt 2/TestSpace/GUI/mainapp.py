import customtkinter as c
from tkinter import ttk  # Import ttk separately for Treeview
import my_queries as mq
import pandas as pd

def mainapp_window():
    master = c.CTk()
    master.title("Material Specifications Table")
    master.geometry("800x800")

    def show_table(liste):
        # Create a Frame for the Treeview (for styling)
        frame1 = c.CTkFrame(master)
        frame1.pack(fill="both", padx= 20, pady=20)  # Pack the frame to make it visible

        # Create Treeview widget with scrollbars inside the CTk frame
        table = ttk.Treeview(frame1, columns=list(liste.columns), show="headings")

        # Define columns and headings
        for col in liste:
            table.heading(col, text=col, command=lambda _col=col: sort_table(_col, False))
            table.column(col, anchor="center", width=100)

        # Insert data into the Treeview
        for _, row in liste.iterrows():
            table.insert("", "end", values=list(row))
        
        # Pack the table and scrollbars in the frame
        table.pack(fill="both", padx= 8, pady=8)

        def sort_table(col, reverse):
            # Get the data from the Treeview
            data = [(table.set(child, col), child) for child in table.get_children('')]
            # Sort the data
            data.sort(reverse=reverse)
            # Rearrange the data in the Treeview
            for index, (val, child) in enumerate(data):
                table.move(child, '', index)
            # Reverse sort next time
            table.heading(col, command=lambda: sort_table(col, not reverse))
        
        

    show_table(mq.material_specifications_data)
    show_table(mq.workers_data)

    # Create a button to close the window
    close_button = c.CTkButton(master, 
                               text="Close", 
                               command=master.destroy)

    # Placements
    close_button.pack()

    # Start the main loop
    master.mainloop()