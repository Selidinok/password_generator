from PyQt6.QtWidgets import QApplication
import sys
from main import MainWindow

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()