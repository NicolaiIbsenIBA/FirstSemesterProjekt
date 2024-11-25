from tkinter import Tk, Label, Entry

# Opret hovedvinduet
root = Tk()
root.title("Login Page")
root.geometry("800x600")  # Sæt en passende vinduesstørrelse
root.configure(bg='#009FE3')  # Baggrundsfarve for hele vinduet

# Opret Label og centrér den
label1 = Label(root, text='Login Page', bg='#009FE3', fg='black', font=('Arial', 24))
label1.pack(pady=20)  # Tilføjer plads øverst for centrering i vinduet

label2 = Label(root, text='UserName:',font=('Arial', 20), bg='#009FE3', fg='White')
label2.place(x=310, y=190)

label3 = Label(root, text='Password:',font=('Arial', 20), bg='#009FE3', fg='White')
label3.place(x=310, y=340)

# Opret indtastningsfelter for brugernavn og adgangskode
entry1 = Entry(root, font=('Arial', 20))  # Indtastningsfelt til brugernavn
entry1.place(x=450, y=190)  # Placer entry1 ved siden af label2

entry2 = Entry(root, show='*', font=('Arial', 20))  # Indtastningsfelt til adgangskode, skjul input
entry2.place(x=450, y=340)  # Placer entry2 ved siden af label3


root.mainloop()