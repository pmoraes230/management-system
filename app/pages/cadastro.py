from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem
)
from backend.database import Database

class CadastroPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.db = Database()  # Conexão com o banco de dados

        # Layout principal
        layout = QVBoxLayout()

        # Formulário de cadastro
        form_layout = QFormLayout()
        self.nome_input = QLineEdit()
        self.cargo_input = QLineEdit()
        self.vt_input = QLineEdit()
        self.va_input = QLineEdit()

        form_layout.addRow("Nome:", self.nome_input)
        form_layout.addRow("Cargo:", self.cargo_input)
        form_layout.addRow("Valor VT:", self.vt_input)
        form_layout.addRow("Valor VA:", self.va_input)

        self.add_button = QPushButton("Adicionar Funcionário")
        self.add_button.clicked.connect(self.add_funcionario)

        # Tabela para listar funcionários
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID", "Nome", "Cargo", "VT", "VA"])

        # Adicionar widgets ao layout principal
        layout.addLayout(form_layout)
        layout.addWidget(self.add_button)
        layout.addWidget(self.table)
        self.setLayout(layout)

        # Atualizar a tabela ao iniciar
        self.update_table()

    def add_funcionario(self):
        """Adiciona um funcionário ao banco."""
        nome = self.nome_input.text()
        cargo = self.cargo_input.text()
        valor_vt = float(self.vt_input.text())
        valor_va = float(self.va_input.text())

        self.db.add_funcionario(nome, cargo, valor_vt, valor_va)
        self.update_table()

    def update_table(self):
        """Atualiza os dados exibidos na tabela."""
        funcionarios = self.db.get_funcionarios()
        self.table.setRowCount(len(funcionarios))

        for row_index, func in enumerate(funcionarios):
            for col_index, value in enumerate(func):
                self.table.setItem(row_index, col_index, QTableWidgetItem(str(value)))
