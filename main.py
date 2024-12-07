# main.py
import tkinter as tk
from ui import AppUI

if __name__ == "__main__":
    root = tk.Tk()
    app = AppUI(root)
    root.mainloop()