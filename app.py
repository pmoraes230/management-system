import tkinter as tk
from database import criar_tabela
from ui import AppUI

# Cria a tabela de funcionários ao iniciar o aplicativo
criar_tabela()

# Configuração da janela principal
root = tk.Tk()
app = AppUI(root)  # Inicializa a interface do usuário

# Inicia o loop principal da interface
root.mainloop()