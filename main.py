from PySide2.QtWidgets import QApplication
from mainwindow import MainWindow
import sys

# Aplicación de Qt
app = QApplication()
# Se crea la ventana
window = MainWindow()
# Se hace visible la ventana
window.show()
sys.exit(app.exec_())