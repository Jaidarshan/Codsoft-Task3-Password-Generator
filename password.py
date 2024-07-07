# Task 3: Password Generator
import tkinter as tk
from tkinter import messagebox
import string
import random
def generate_password():
    try:
        length=int(entry_length.get())
        if length<1:
            messagebox.showerror("Error","Password length must be at least 1")
            return
    except ValueError:
        messagebox.showerror("Error","Please enter a valid number")
        return
    characters=string.ascii_letters+string.digits+string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    entry_password.delete(0,tk.END)
    entry_password.insert(0,password)
window=tk.Tk()
window.title("Password Generator")
window.geometry("410x320")
head_length=tk.Label(window,text="Password Generator",font=("Helvetica",20,"bold"))
head_length.pack(pady=10)
label_length=tk.Label(window,text="Enter the length of the password:",font=("Helvetica",14))
label_length.pack(pady=10)
entry_length=tk.Entry(window,font=("Helvetica",14))
entry_length.pack(pady=5)
button_generate=tk.Button(window,text="Generate Password",command=generate_password,bg="blue",fg="white",font=("Helvetica",14))
button_generate.pack(pady=10)
password_label=tk.Label(window,text="Password:",font=("Helvetica",14))
password_label.pack(pady=10)
entry_password=tk.Entry(window,width=35,font=("Helvetica",14))
entry_password.pack(pady=5)
window.mainloop()
