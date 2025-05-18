import sys
import pandas as pd
from PyQt6.QtCore import Qt

from PyQt6.QtWidgets import QTabWidget, QMainWindow, QWidget, QVBoxLayout, QApplication, QTableWidget, QTableWidgetItem

from IU.view_tab1 import ViewTable1
from IU.view_tab3 import WievTable3
from data_tab import Model


class WievModel(QMainWindow):
    model = Model()
    def __init__(self, model_new):
        super().__init__()
        self.setWindowTitle("Приложение с вкладками")
        self.setGeometry(100, 100, 600, 400)

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.tab1 = QWidget()  # Первая вкладка
        self.tab3 = QWidget()  # Вторая вкладка
        self.tab4 = QWidget()
        self.tab5 = QWidget()
        self.tab6 = QWidget()

        self.tabs.addTab(self.tab1, "Модель последняя")
        self.tabs.addTab(self.tab3, "Затраты по маслу в сх")
        self.tabs.addTab(self.tab4, "Затраты по маслу в пр")
        self.tabs.addTab(self.tab5, "Регулирующий блок")
        self.tabs.addTab(self.tab6, "Управляющий блок")

        self.init_table1_tab()
        #self.init_table3_tab()
        #self.init_table4_tab()
        #self.init_table5_tab()
        #self.init_table6_tab()

    def init_table1_tab(self):
        layout = QVBoxLayout()
        table_widget = ViewTable1(self.model.tab1)
        self.tab1.addWidget(table_widget)

        tab_content = QWidget()
        tab_content.setLayout(layout)

    def init_table3_tab(self):
        layout = QVBoxLayout()
        self.tab3 = WievTable3(self.model.tab3)
        layout.addWidget(self.tab3)
        self.tab3.setLayout(layout)


if __name__ == "__main__":
    model = Model()
    app = QApplication(sys.argv)
    window = WievModel(model)
    window.show()
    sys.exit(app.exec())