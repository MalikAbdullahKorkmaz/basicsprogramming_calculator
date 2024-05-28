import tkinter as tk
from tkinter import messagebox

def add():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result.set(num1 + num2)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

def subtract():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result.set(num1 - num2)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

def multiply():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result.set(num1 * num2)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

def divide():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if num2 == 0:
            messagebox.showerror("Math error", "Cannot divide by zero.")
        else:
            result.set(num1 / num2)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

# Create main window
root = tk.Tk()
root.title("Simple Calculator")

# Create StringVar to hold the result
result = tk.StringVar()

# Create and place widgets
tk.Label(root, text="Number 1:").grid(row=0, column=0, padx=10, pady=5)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Number 2:").grid(row=1, column=0, padx=10, pady=5)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=5)

tk.Button(root, text="Add", command=add).grid(row=2, column=0, padx=10, pady=5)
tk.Button(root, text="Subtract", command=subtract).grid(row=2, column=1, padx=10, pady=5)
tk.Button(root, text="Multiply", command=multiply).grid(row=3, column=0, padx=10, pady=5)
tk.Button(root, text="Divide", command=divide).grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Result:").grid(row=4, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=result, state='readonly').grid(row=4, column=1, padx=10, pady=5)

# Run the main loop
root.mainloop()
