import tkinter as tk
from tkinter import messagebox

def add():
    result.set(float(entry1.get()) + float(entry2.get()))

def subtract():
    result.set(float(entry1.get()) - float(entry2.get()))

def multiply():
    result.set(float(entry1.get()) * float(entry2.get()))

def divide():
    try:
        result.set(float(entry1.get()) / float(entry2.get()))
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero")

# Main window
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("500x500")

# Input
tk.Label(window, text="Enter First Number").pack()
entry1 = tk.Entry(window)
entry1.pack()

tk.Label(window, text="Enter Second Number").pack()
entry2 = tk.Entry(window)
entry2.pack()

# Buttons
tk.Button(window, text="+", command=add).pack(pady=5)
tk.Button(window, text="-", command=subtract).pack(pady=5)
tk.Button(window, text="x", command=multiply).pack(pady=5)
tk.Button(window, text="/", command=divide).pack(pady=5)

# Result
result = tk.StringVar()
tk.Label(window, text="Result:").pack()
tk.Label(window, textvariable=result, font=("Arial", 16)).pack()

window.mainloop()

           


