import sys

import pandas as pd
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QMainWindow, QApplication

from data_tab import Model


class ViewTable5(QTableWidget):
    tabel1= pd.DataFrame()
    def __init__(self, tabel5):
        super().__init__()

        self.setRowCount(21)  # 4 строки
        self.setColumnCount(10)  # 3 столбца

        item = QTableWidgetItem("Показатели")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setSpan(0,0,4,1)
        self.setItem(0,0,item)

        item = QTableWidgetItem("Исходные данные")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setSpan(0,1,4,1)
        self.setItem(0,1,item)

        item = QTableWidgetItem("Варианты реализации продукции")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setSpan(0,2,1,8)
        self.setItem(0,2,item)

        item = QTableWidgetItem("маслосемян")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setSpan(1,2,1,2)
        self.setItem(1,2,item)

        item = QTableWidgetItem("масла подсолнечного")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setSpan(1,4,1,6)
        self.setItem(1,4,item)

        item = QTableWidgetItem("внутренний рынок")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setSpan(2,2,2,1)
        self.setItem(2,2,item)

        item = QTableWidgetItem("экспорт")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setSpan(2,3,2,1)
        self.setItem(2,3,item)

        item = QTableWidgetItem("собственная переработка")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setSpan(2,4,1,4)
        self.setItem(2,4,item)

        item = QTableWidgetItem("промышленная переработка")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setSpan(2,8,1,2)
        self.setItem(2,8,item)

        item = QTableWidgetItem("для собственных нужд")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(3,4,item)

        item = QTableWidgetItem("оплата услуг по пе-реработке даваль-ческого сырья")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(3,5,item)

        item = QTableWidgetItem("внутренний рынок")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(3,6,item)

        item = QTableWidgetItem("экспорт")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(3,7,item)

        item = QTableWidgetItem("внутренний рынок ")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(3,8,item)

        item = QTableWidgetItem("экспорт")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(3,9,item)


        item = QTableWidgetItem("Посевная площадь, га")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(4,0,item)

        item = QTableWidgetItem("Урожайность, ц/га")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(5,0,item)

        item = QTableWidgetItem("Выход продукции всего, ц")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(6,0,item)

        item = QTableWidgetItem("Себестоимость 1 ц, руб")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(7,0,item)

        item = QTableWidgetItem("Себестоимость всего, тыс.руб")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(8,0,item)

        item = QTableWidgetItem("Корректирующие коэффициенты распределения исходного сырья по:")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(9,0,item)

        item = QTableWidgetItem("виду продукции")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(10,0,item)

        item = QTableWidgetItem("способам переработки")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(11,0,item)

        item = QTableWidgetItem("каналам реализации")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(12,0,item)

        item = QTableWidgetItem("выходу сырья")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(13,0,item)

        item = QTableWidgetItem("себестоимости сырья для переработки")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(14,0,item)

        item = QTableWidgetItem("выходу готовой продукции")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(15,0,item)

        item = QTableWidgetItem("затратам на переработку и доработку маслосемян")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(16,0,item)

        item = QTableWidgetItem("товарности")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(17,0,item)

        item = QTableWidgetItem("транспортным расходам на реализацию")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(18,0,item)

        item = QTableWidgetItem("затратам, связанным с реализацией продукции")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(19,0,item)

        item = QTableWidgetItem("по средней цене единицы продукции")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(20,0,item)



        # Данные для таблицы (можно заменить на свои)
        data = tabel5

        # Заполняем таблицу
        for row_idx, row_data in enumerate(list(data.columns)):
            for col_idx, cell_data in enumerate(data[row_data]):
                if type(cell_data) == float:
                    item = QTableWidgetItem("{:.2f}".format(float(cell_data)))
                    item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)  # Запрет редактирования
                else:
                    item = QTableWidgetItem(cell_data)
                    item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)  # Запрет редактирования
                self.setItem(col_idx+4, row_idx+1, item)

class TableWindowM(QMainWindow):
    tabel1 = pd.DataFrame()

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
        self.table = ViewTable3(tab)

        layout.addWidget(self.table)



if __name__ == "__main__":
    model_test = Model()
    model_test.calculate_model()
    app = QApplication(sys.argv)
    window = TableWindowM(model_test.tab5)
    window.show()
    sys.exit(app.exec())