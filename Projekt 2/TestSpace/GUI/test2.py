import tkinter as tk
from tkinter import ttk
tkwindow = tk.Tk()
cbox = ttk.Combobox(tkwindow, values=[1,2,3], state='readonly')
cbox.pack()

def callback(*args):
    print(cbox.get())

cbox.bind("<<ComboboxSelected>>", callback)
btn = ttk.Button(tkwindow, text="Call Callback", command=callback)
btn.pack()

tkwindow.mainloop()