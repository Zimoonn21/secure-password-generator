import random
import string
import tkinter as tk
from tkinter import messagebox


def generate():
  try:
    length = int(entry.get())
    if length <= 5:
      messagebox.showerror("Error", "Please choose a number larger than 5!")
      return
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    result_label.config(text=f"Password: {password}")
  except ValueError:
    messagebox.showerror("Error", "Please enter a valid number!")


root = tk.Tk()
root.title("Secure Password Generator")
root.geometry("400x320")
root.resizable(False, False)
root.config(bg="#1f2428")  # Tło okna (GitHub)

tk.Label(
    root,
    text="Enter password length:",
    font=("Arial", 15),
    bg="#1f2428",
    fg="#c9d1d9",
).pack(pady=10)

entry = tk.Entry(
    root,
    font=("Arial", 15),
    justify="center",
    bg="#333333",
    fg="#c9d1d9",
    insertbackground="white",
)
entry.insert(0, "12")
entry.pack(pady=5)

btn = tk.Button(
    root,
    text="Generate Password",
    command=generate,
    font=("Arial", 15, "bold"),
    bg="#28a745",
    fg="#ffffff",
)
btn.pack(pady=15)

result_label = tk.Label(
    root, text="", font=("Courier", 15, "bold"), bg="#1f2428", fg="#58a6ff"
)
result_label.pack(pady=10)

root.mainloop()