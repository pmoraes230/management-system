from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QWidget
from app.pages.cadastro import CadastroPage  # Importando a página de cadastro

class Sidebar(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setFixedWidth(200)

        # Layout da barra lateral
        layout = QVBoxLayout(self)

        # Botão Home
        btn_home = QPushButton("Home")
        btn_home.clicked.connect(lambda: self.main_window.switch_page(self.main_window.pages["home"]))
        layout.addWidget(btn_home)

        # Botão Cadastro
        btn_cadastro = QPushButton("Cadastro")
        btn_cadastro.clicked.connect(lambda: self.main_window.switch_page(self.main_window.pages["cadastro"]))
        layout.addWidget(btn_cadastro)

        # Botão Consulta
        btn_consulta = QPushButton("Consulta")
        btn_consulta.clicked.connect(lambda: self.main_window.switch_page(self.main_window.pages["consulta"]))
        layout.addWidget(btn_consulta)

        layout.addStretch()
