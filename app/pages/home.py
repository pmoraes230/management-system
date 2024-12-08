from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class HomePage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Layout da página inicial
        layout = QVBoxLayout(self)
        
        # Título principal
        title = QLabel("Bem-vindo ao Gerenciador de VT e VA!")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("Arial", 18, QFont.Bold))
        layout.addWidget(title)

        # Subtítulo com uma breve descrição
        subtitle = QLabel("Gerencie de forma prática e eficiente seus benefícios de Transporte e Alimentação.")
        subtitle.setAlignment(Qt.AlignCenter)
        layout.addWidget(subtitle)

        # Adicionando uma breve descrição dos benefícios
        description = QLabel(
            "Com o Gerenciador de VT e VA, você pode cadastrar, consultar e acompanhar os valores dos benefícios, "
            "tornando o processo mais rápido e organizado."
        )
        description.setWordWrap(True)  # Permite que o texto quebre para novas linhas
        description.setAlignment(Qt.AlignCenter)
        layout.addWidget(description)

        # Adicionando um botão para acessar a página de consulta
        button_layout = QHBoxLayout()
        
        btn_consulta = QPushButton("Consultar Benefícios", self)
        btn_consulta.setFont(QFont("Arial", 12))
        btn_consulta.clicked.connect(self.open_consulta_page)
        button_layout.addWidget(btn_consulta)

        # Adicionando o botão ao layout
        layout.addLayout(button_layout)

        # Outro botão para ir para o cadastro (por exemplo)
        btn_cadastro = QPushButton("Cadastrar Novo Benefício", self)
        btn_cadastro.setFont(QFont("Arial", 12))
        btn_cadastro.clicked.connect(self.open_cadastro_page)
        layout.addWidget(btn_cadastro)

    def open_consulta_page(self):
        """Método que pode ser chamado para redirecionar para a página de consulta"""
        print("Abrir página de consulta...")  # Aqui você pode implementar a navegação

    def open_cadastro_page(self):
        """Método que pode ser chamado para redirecionar para a página de cadastro"""
        print("Abrir página de cadastro...")  # Aqui você pode implementar a navegação
