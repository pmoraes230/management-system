# styles.py
from tkinter import ttk

def apply_styles(root):
    root.configure(bg="#e0e0e0")  # Cor de fundo da janela principal

    style = ttk.Style()
    style.configure("TButton", padding=6, relief="flat", background="#4CAF50", foreground="white")
    style.map("TButton", background=[("active", "#45a049")])  # Cor ao passar o mouse