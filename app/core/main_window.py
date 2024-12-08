from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from app.components.sidebar import Sidebar
from app.pages.home import HomePage
from app.pages.cadastro import CadastroPage
from app.pages.consulta import ConsultaPage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gerenciador de VT e VA")
        self.setGeometry(100, 100, 1024, 768)

        # Layout principal
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout vertical principal
        self.main_layout = QVBoxLayout(central_widget)

        # Inicializar as páginas
        self.pages = {
            "home": HomePage(self),
            "cadastro": CadastroPage(self),
            "consulta": ConsultaPage(self)
        }

        # Página inicial
        self.current_page = self.pages["home"]
        self.main_layout.addWidget(self.current_page)

        # Barra lateral
        self.sidebar = Sidebar(self)
        self.main_layout.addWidget(self.sidebar)

    def switch_page(self, new_page):
        """Mudar para outra página dinamicamente."""
        self.main_layout.removeWidget(self.current_page)  # Remove a página atual do layout
        self.current_page.setParent(None)  # Remove a página da interface
        self.current_page = new_page  # Atualiza para a nova página (já é uma instância)
        self.main_layout.addWidget(self.current_page)  # Adiciona a nova página