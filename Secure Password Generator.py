import random, string
import tkinter as tk
from tkinter import messagebox

def generate():
    try:
        n = int(e.get())
        if n < 6:
            messagebox.showerror("Error", "Min 6 characters!")
            return
        
        haslo = "".join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=n))
        lbl.config(text=haslo)
    except:
        messagebox.showerror("Error", "Enter a number!")

root = tk.Tk()
root.title("SecurePasswordGenerator")
root.geometry("350x250")
root.config(bg="#1f2428")

tk.Label(root, text="Length:", bg="#1f2428", fg="white").pack(pady=10)

e = tk.Entry(root, justify="center", bg="#333", fg="white", insertbackground="white")
e.insert(0, "10")
e.pack(pady=5)

tk.Button(root, text="Generate", command=generate, bg="#28a745", fg="white").pack(pady=10)

lbl = tk.Label(root, text="", bg="#1f2428", fg="#58a6ff", font=("Courier", 12))
lbl.pack(pady=10)

root.mainloop()