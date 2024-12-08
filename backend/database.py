import sqlite3

class Database:
    def __init__(self, db_name="gerenciador_vtva.db"):
        self.db_name = db_name
        self.conn = None
        self.connect()

    def connect(self):
        """Estabelece conexão com o banco de dados."""
        self.conn = sqlite3.connect(self.db_name)
        self.create_tables()

    def create_tables(self):
        """Cria as tabelas necessárias no banco."""
        query = """
        CREATE TABLE IF NOT EXISTS funcionarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cargo TEXT NOT NULL,
            valor_vt REAL NOT NULL,
            valor_va REAL NOT NULL
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def add_funcionario(self, nome, cargo, valor_vt, valor_va):
        """Adiciona um funcionário ao banco."""
        query = """
        INSERT INTO funcionarios (nome, cargo, valor_vt, valor_va)
        VALUES (?, ?, ?, ?)
        """
        self.conn.execute(query, (nome, cargo, valor_vt, valor_va))
        self.conn.commit()

    def get_funcionarios(self):
        """Obtém todos os funcionários."""
        query = "SELECT * FROM funcionarios"
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def update_funcionario(self, id, nome, cargo, valor_vt, valor_va):
        """Atualiza os dados de um funcionário."""
        query = """
        UPDATE funcionarios
        SET nome = ?, cargo = ?, valor_vt = ?, valor_va = ?
        WHERE id = ?
        """
        self.conn.execute(query, (nome, cargo, valor_vt, valor_va, id))
        self.conn.commit()

    def delete_funcionario(self, id):
        """Remove um funcionário do banco."""
        query = "DELETE FROM funcionarios WHERE id = ?"
        self.conn.execute(query, (id,))
        self.conn.commit()

    def close(self):
        """Fecha a conexão com o banco."""
        if self.conn:
            self.conn.close()
