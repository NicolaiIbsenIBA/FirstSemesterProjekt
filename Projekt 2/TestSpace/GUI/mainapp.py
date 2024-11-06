import customtkinter as c
from tkinter import ttk  # Import ttk separately for Treeview
import my_queries as mq


def mainapp_window():
    master = c.CTk()
    master.title("Material Specifications Table")
    master.geometry("800x800")

    def show_table(liste):
        # Create a Frame for the Treeview (for styling)
        frame1 = c.CTkFrame(master)

        # Create Treeview widget with scrollbars inside the CTk frame
        table = ttk.Treeview(frame1, columns=list(liste.columns), show="headings")

        # Define columns and headings
        for col in liste:
            table.heading(col, text=col)
            table.column(col, anchor="center", width=100)

        # Insert data into the Treeview
        for _, row in liste.iterrows():
            table.insert("", "end", values=list(row))
        
        # Pack the table and scrollbars in the frame
        table.grid(row=0, column=0, sticky="nsew")

        # Configure frame to expand with window resizing
        frame1.grid_rowconfigure(0, weight=0)
        frame1.grid_columnconfigure(0, weight=1)

        frame1.pack(fill="both", padx=20, pady=20)
        table.pack(fill="both", padx=5, pady=5)

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