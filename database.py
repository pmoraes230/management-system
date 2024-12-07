import sqlite3

def conectar():
    conn = sqlite3.connect('empresa.db')
    return conn

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS funcionarios
                      (id INTEGER PRIMARY KEY, nome TEXT, cargo TEXT)''')
    conn.commit()
    conn.close()

def adicionar_funcionario(nome, cargo):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO funcionarios (nome, cargo) VALUES (?, ?)", (nome, cargo))
    conn.commit()
    conn.close()

def listar_funcionarios():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM funcionarios")
    funcionarios = cursor.fetchall()
    conn.close()
    return funcionarios