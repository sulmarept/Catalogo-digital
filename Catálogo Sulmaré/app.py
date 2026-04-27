import sys
import os
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl, Qt
from PyQt6.QtGui import QIcon

class MainWindow(QWebEngineView):
    def __init__(self):
        super().__init__()
        
        # Título da janela
        self.setWindowTitle("Catálogo Sulmaré 2026")
        
        # Ícone (coloca o teu logo aqui)
        icon_path = os.path.join(os.path.dirname(__file__), "imagens", "logo-sulmare.svg")
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        
        # Carrega o index.html
        base_path = os.path.dirname(os.path.abspath(__file__))
        index_path = os.path.join(base_path, "index.html")
        self.load(QUrl.fromLocalFile(index_path))
        
        # Tamanho inicial da janela
        self.resize(1280, 800)
        self.showMaximized()   # Abre maximizado

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())