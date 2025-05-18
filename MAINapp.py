import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget

from IU.main_screen import MainScreen

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainScreen()
    window.show()
    sys.exit(app.exec())
