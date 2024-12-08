from PyQt5.QtWidgets import (
    QLabel, QVBoxLayout, QHBoxLayout, QFrame, QPushButton, QWidget, QSpacerItem, QSizePolicy
)
from PyQt5.QtChart import QChart, QChartView, QPieSeries
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter

class HomePage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Layout Principal
        main_layout = QVBoxLayout(self)
        
        # NavBar
        navbar = QHBoxLayout()
        navbar.setContentsMargins(0, 0, 0, 10)
        navbar.setSpacing(15)
        
        title = QLabel("Gerenciador de VT e VA")
        title.setObjectName("navbar_title")
        navbar.addWidget(title)
        
        btn_dashboard = QPushButton("Dashboard")
        btn_dashboard.setObjectName("btn_dashboard")
        navbar.addWidget(btn_dashboard)
        
        btn_sair = QPushButton("Sair")
        btn_sair.setObjectName("btn_sair")
        navbar.addWidget(btn_sair)
        
        main_layout.addLayout(navbar)
        
        # Main Content
        content_layout = QHBoxLayout()
        content_layout.setSpacing(20)
        
        # Informações no lado esquerdo
        info_layout = QVBoxLayout()
        info_layout.setSpacing(15)
        
        welcome_label = QLabel("Bem vindo(a) ao gerenciador de VT e VA!")
        welcome_label.setObjectName("label_welcome")
        info_layout.addWidget(welcome_label)
        
        details_label = QLabel(
            "Aqui você pode gerenciar eficientemente os benefícios de VT e VA da sua empresa."
        )
        details_label.setWordWrap(True)
        details_label.setObjectName("details_label")
        info_layout.addWidget(details_label)
        
        # Gráfico do lado direito
        chart_layout = QVBoxLayout()
        chart_layout.setSpacing(10)
        
        # Gráfico de pizza (Exemplo VA)
        va_chart = self.create_pie_chart("Uso do VA", {"Alimentação": 50, "Restaurantes": 30, "Outros": 10})
        chart_layout.addWidget(va_chart)
        
        # Gráfico de pizza (Exemplo VT)
        vt_chart = self.create_pie_chart("Uso do VT", {"Ônibus": 50, "Metrô": 40, "Outros": 10})
        chart_layout.addWidget(vt_chart)
        
        # Adicionando layout ao conteúdo principal
        content_layout.addLayout(info_layout, 2)
        content_layout.addLayout(chart_layout, 3)
        
        main_layout.addLayout(content_layout)
        
        # Footer
        footer = QVBoxLayout()
        footer.setContentsMargins(0, 10, 0, 0)
        
        copyright_label = QLabel("2024 Gerenciador de VT e VA - Todos os direitos reservados.")
        copyright_label.setObjectName("copyright_label")
        footer.addWidget(copyright_label)
        
        spacer_footer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        footer.addSpacerItem(spacer_footer)
        
        support_label = QLabel("Suporte: suporte@empresa.com")
        support_label.setObjectName("support_label")
        footer.addWidget(support_label)
        
        main_layout.addLayout(footer)
        
    def create_pie_chart(self, title, data):
        """Criar um gráfico de pizza com os dados fornecidos"""
        series = QPieSeries()
        for label, value in data.items():
            series.append(label, value)
            
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle(title)
        chart.legend().setAlignment(Qt.AlignBottom)
        
        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)  # Corrigido para usar QPainter
        
        frame = QFrame()
        frame_layout = QVBoxLayout(frame)
        frame_layout.addWidget(chart_view)
        
        return frame
