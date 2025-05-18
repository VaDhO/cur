import sys
import pandas as pd
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget
)
from PyQt6.QtCore import Qt

from data_tab import Model


class TableWindowM(QMainWindow):
    tab = pd.DataFrame()

    def __init__(self, tab):
        super().__init__()
        self.setWindowTitle("Пример таблицы в PyQt6")
        self.setGeometry(100, 100, 600, 400)

        # Создаем центральный виджет и layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Создаем таблицу
        self.table = QTableWidget()
        self.table.setRowCount(tab.shape[0])  # 4 строки
        self.table.setColumnCount(tab.shape[1])  # 3 столбца
        layout.addWidget(self.table)

        # Заполняем таблицу данными
        self.fill_table(tab)

    def fill_table(self,tab):
        # Устанавливаем заголовки столбцов
        headers = list(tab.columns)
        self.table.setHorizontalHeaderLabels(headers)

        # Данные для таблицы (можно заменить на свои)
        data = tab


        # Заполняем таблицу
        for row_idx, row_data in enumerate(list(data.columns)):
            for col_idx, cell_data in enumerate(data[row_data]):
                if type(cell_data) == float:
                    item = QTableWidgetItem("{:.2f}".format(float(cell_data)))
                    item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)  # Запрет редактирования
                else:
                    item = QTableWidgetItem(cell_data)
                    item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)  # Запрет редактирования
                self.table.setItem(col_idx, row_idx, item)


if __name__ == "__main__":
    model_test = Model()
    model_test.calculate_model()
    app = QApplication(sys.argv)
    window = TableWindowM(model_test.tab5)
    window.show()
    sys.exit(app.exec())
