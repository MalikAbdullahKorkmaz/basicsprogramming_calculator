# main_program.py

import tkinter as tk
from calculator_module import Calculator

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()