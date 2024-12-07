# ui.py
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from database import adicionar_funcionario, listar_funcionarios
from style import apply_styles

class AppUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciamento de Funcionários")
        self.root.geometry("400x400")
        apply_styles(self.root)  # Aplica os estilos

        # Frame para adicionar funcionários
        self.frame_adicionar = ttk.Frame(root, padding="10")
        self.frame_adicionar.pack(pady=10)

        label_nome = ttk.Label(self.frame_adicionar, text="Nome:")
        label_nome.grid(row=0, column=0)
        self.entry_nome = ttk.Entry(self.frame_adicionar)
        self.entry_nome.grid(row=0, column=1)

        label_cargo = ttk.Label(self.frame_adicionar, text="Cargo:")
        label_cargo.grid(row=1, column=0)
        self.entry_cargo = ttk.Entry(self.frame_adicionar)
        self.entry_cargo.grid(row=1, column=1)

        button_adicionar = ttk.Button(self.frame_adicionar, text="Adicionar Funcionário", command=self.adicionar)
        button_adicionar.grid(row=2, columnspan=2)

        # Frame para listar funcionários
        self.frame_lista = ttk.Frame(root, padding="10")
        self.frame_lista.pack(pady=10)

        self.listar()  # Chama a função para listar funcionários

    def adicionar(self):
        nome = self.entry_nome.get()
        cargo = self.entry_cargo.get()
        if nome and cargo:
            adicionar_funcionario(nome, cargo)
            self.entry_nome.delete(0, tk.END)
            self.entry_cargo.delete(0, tk.END)
            self.listar()
        else:
            messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")

    def listar(self):
        for widget in self.frame_lista.winfo_children():
            widget.destroy()
        
        funcionarios = listar_funcionarios()
        for funcionario in funcionarios:
            label = ttk.Label(self.frame_lista, text=f"{funcionario[1]} - {funcionario[2]}")
            label.pack()