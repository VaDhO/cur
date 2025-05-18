import sys
import pandas as pd
from PyQt6.QtCore import Qt

from PyQt6.QtWidgets import QTabWidget, QMainWindow, QWidget, QVBoxLayout, QApplication, QTableWidget, QTableWidgetItem

from IU.view_tab1 import ViewTable1
from IU.view_tab3 import ViewTable3
from data_tab import Model


class WievModel(QMainWindow):
    model = Model()
    def __init__(self, model_new):
        super().__init__()
        self.setWindowTitle("Приложение с вкладками")
        self.setGeometry(100, 100, 600, 400)

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        # Создаем вкладки и добавляем сразу с содержимым
        self.add_table_tab(ViewTable1(model_new.tab1), "Модель последняя")
        self.add_table_tab(ViewTable3(model_new.tab3), "Затраты по маслу в сх")
        self.add_table_tab(ViewTable3(model_new.tab4), "Затраты по маслу в пр")
        self.add_table_tab(QWidget(), "Регулирующий блок")
        self.add_table_tab(QWidget(), "Управляющий блок")

    def add_table_tab(self, widget, title):
        layout = QVBoxLayout()
        layout.addWidget(widget)
        container = QWidget()
        container.setLayout(layout)
        self.tabs.addTab(container, title)


if __name__ == "__main__":
    model = Model()
    app = QApplication(sys.argv)
    window = WievModel(model)
    window.show()
    sys.exit(app.exec())