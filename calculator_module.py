# calculator_module.py

import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced calculator")
        
        self.num1_label = tk.Label(root, text="number 1:", font=('Arial', 12))
        self.num1_label.grid(row=0, column=0, padx=10, pady=5)
        self.num1_entry = tk.Entry(root, font=('Arial', 12))
        self.num1_entry.grid(row=0, column=1, padx=10, pady=5)

        self.num2_label = tk.Label(root, text="number 2:", font=('Arial', 12))
        self.num2_label.grid(row=1, column=0, padx=10, pady=5)
        self.num2_entry = tk.Entry(root, font=('Arial', 12))
        self.num2_entry.grid(row=1, column=1, padx=10, pady=5)

        self.result_label = tk.Label(root, text="result:", font=('Arial', 12))
        self.result_label.grid(row=2, column=0, padx=10, pady=5)
        self.result = tk.StringVar()
        self.result_entry = tk.Entry(root, textvariable=self.result, state='readonly', font=('Arial', 12))
        self.result_entry.grid(row=2, column=1, padx=10, pady=5)

        self.add_button = tk.Button(root, text="Add", command=self.add, font=('Arial', 12), bg='lightblue')
        self.add_button.grid(row=3, column=0, padx=10, pady=5)
        self.subtract_button = tk.Button(root, text="Subtractions", command=self.subtract, font=('Arial', 12), bg='lightgreen')
        self.subtract_button.grid(row=3, column=1, padx=10, pady=5)
        self.multiply_button = tk.Button(root, text="Multiplication", command=self.multiply, font=('Arial', 12), bg='lightyellow')
        self.multiply_button.grid(row=4, column=0, padx=10, pady=5)
        self.divide_button = tk.Button(root, text="division", command=self.divide, font=('Arial', 12), bg='lightcoral')
        self.divide_button.grid(row=4, column=1, padx=10, pady=5)
        self.clear_button = tk.Button(root, text="Clean_up", command=self.clear, font=('Arial', 12), bg='lightgray')
        self.clear_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

    def get_inputs(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            return num1, num2
        except ValueError:
            messagebox.showerror("Invalid entry", "Please enter valid numbers.")
            return None, None

    def add(self):
        num1, num2 = self.get_inputs()
        if num1 is not None and num2 is not None:
            self.result.set(num1 + num2)

    def subtract(self):
        num1, num2 = self.get_inputs()
        if num1 is not None and num2 is not None:
            self.result.set(num1 - num2)

    def multiply(self):
        num1, num2 = self.get_inputs()
        if num1 is not None and num2 is not None:
            self.result.set(num1 * num2)

    def divide(self):
        num1, num2 = self.get_inputs()
        if num1 is not None and num2 is not None:
            if num2 == 0:
                messagebox.showerror("Math error", "Cannot divide by zero")
            else:
                self.result.set(num1 / num2)

    def clear(self):
        self.num1_entry.delete(0, tk.END)
        self.num2_entry.delete(0, tk.END)
        self.result.set("")

# This will be used to test the module independently
if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
