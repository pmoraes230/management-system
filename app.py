import tkinter as tk
from tkinter import messagebox
from database import criar_tabela, adicionar_funcionario, listar_funcionarios

# Cria a tabela de funcionários ao iniciar o aplicativo
criar_tabela()

def adicionar():
    nome = entry_nome.get()
    cargo = entry_cargo.get()
    if nome and cargo:
        adicionar_funcionario(nome, cargo)
        entry_nome.delete(0, tk.END)
        entry_cargo.delete(0, tk.END)
        listar()
    else:
        messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")

def listar():
    for widget in frame_lista.winfo_children():
        widget.destroy()
    
    funcionarios = listar_funcionarios()
    for funcionario in funcionarios:
        label = tk.Label(frame_lista, text=f"{funcionario[1]} - {funcionario[2]}")
        label.pack()

# Configuração da janela principal
root = tk.Tk()
root.title("Gerenciamento de Funcionários")
root.geometry("400x400")

# Frame para adicionar funcionários
frame_adicionar = tk.Frame(root)
frame_adicionar.pack(pady=10)

label_nome = tk.Label(frame_adicionar, text="Nome:")
label_nome.grid(row=0, column=0)
entry_nome = tk.Entry(frame_adicionar)
entry_nome.grid(row=0, column=1)

label_cargo = tk.Label(frame_adicionar, text="Cargo:")
label_cargo.grid(row=1, column=0)
entry_cargo = tk.Entry(frame_adicionar)
entry_cargo.grid(row=1, column=1)

button_adicionar = tk.Button(frame_adicionar, text="Adicionar Funcionário", command=adicionar)
button_adicionar.grid(row=2, columnspan=2)

# Frame para listar funcionários
frame_lista = tk.Frame(root)
frame_lista.pack(pady=10)

listar()  # Chama a função para listar funcionários

# Inicia o loop principal da interface
root.mainloop()