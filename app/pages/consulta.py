from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt

class ConsultaPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Layout da página de consulta
        layout = QVBoxLayout(self)

        # Título da página
        label = QLabel("Página de Consulta")
        layout.addWidget(label)

        # Campo de pesquisa
        self.search_field = QLineEdit(self)
        self.search_field.setPlaceholderText("Digite o termo para consultar...")
        layout.addWidget(self.search_field)

        # Botão de consulta
        self.search_button = QPushButton("Consultar", self)
        self.search_button.clicked.connect(self.perform_query)  # Conecta ao método de consulta
        layout.addWidget(self.search_button)

        # Tabela para exibir os resultados
        self.result_table = QTableWidget(self)
        self.result_table.setColumnCount(3)  # 3 colunas para exibir os dados
        self.result_table.setHorizontalHeaderLabels(["ID", "Nome", "Descrição"])
        layout.addWidget(self.result_table)

    def perform_query(self):
        """Simula uma consulta e exibe os resultados na tabela."""
        
        # Obter o termo da pesquisa
        search_term = self.search_field.text().strip()

        # Simulação de resultados (em um caso real, isso seria obtido do banco de dados)
        results = [
            {"id": 1, "name": "Restaurante A", "description": "Restaurante italiano."},
            {"id": 2, "name": "Praia B", "description": "Praia com água cristalina."},
            {"id": 3, "name": "Museu C", "description": "Museu de arte moderna."}
        ]

        # Filtrando os resultados com base no termo de pesquisa
        filtered_results = [res for res in results if search_term.lower() in res["name"].lower()]

        # Limpando a tabela antes de adicionar novos resultados
        self.result_table.setRowCount(0)

        # Preenchendo a tabela com os resultados
        for row_index, result in enumerate(filtered_results):
            self.result_table.insertRow(row_index)
            self.result_table.setItem(row_index, 0, QTableWidgetItem(str(result["id"])))
            self.result_table.setItem(row_index, 1, QTableWidgetItem(result["name"]))
            self.result_table.setItem(row_index, 2, QTableWidgetItem(result["description"]))

        # Caso não haja resultados, exibe uma mensagem na tabela
        if not filtered_results:
            self.result_table.setRowCount(1)
            self.result_table.setItem(0, 0, QTableWidgetItem("Nenhum resultado encontrado"))
            self.result_table.setSpan(0, 0, 1, 3)
            self.result_table.setItem(0, 0, QTableWidgetItem("Nenhum resultado encontrado"))
