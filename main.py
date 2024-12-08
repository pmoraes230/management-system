import sys
from PyQt5.QtWidgets import QApplication
from app.core.main_window import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Carregar estilos globais (QSS)
    with open("app/styles/main.qss", "r") as f:
        app.setStyleSheet(f.read())
    
    # Inicializar janela principal
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())
