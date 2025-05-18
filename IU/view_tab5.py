import sys

import pandas as pd
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QMainWindow, QApplication

from data_tab import Model


class ViewTable3(QTableWidget):
    tabel1= pd.DataFrame()
    def __init__(self, tabel3):
        super().__init__()

        self.setRowCount(21)  # 4 строки
        self.setColumnCount(10)  # 3 столбца

        item = QTableWidgetItem("Показатели")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setSpan(0,0,3,2)
        self.setItem(0,0,item)

        item = QTableWidgetItem("Этапы формирования и доставки груза")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setSpan(0,2,1,7)
        self.setItem(0,2,item)

        item = QTableWidgetItem("название")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(3,0,item)

        item = QTableWidgetItem("ед. Изм")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(3,1,item)

        item = QTableWidgetItem("I маршрут ")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setSpan(1,2,1,2)
        self.setItem(1,2,item)

        item = QTableWidgetItem("II маршрут")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setSpan(1,4,1,3)
        self.setItem(1,4,item)

        item = QTableWidgetItem("всего затрат")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setSpan(1,7,1,2)
        self.setItem(1,7,item)

        item = QTableWidgetItem("Всего")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setSpan(0,9,4,1)
        self.setItem(0,9,item)

        item = QTableWidgetItem("до элеватора автомобильным транспортом")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setSpan(2,2,2,1)
        self.setItem(2,2,item)

        item = QTableWidgetItem("до пункта назначения по железной дороге")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setSpan(2,3,2,1)
        self.setItem(2,3,item)

        item = QTableWidgetItem("до речного порта")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setSpan(2,4,2,1)
        self.setItem(2,4,item)

        item = QTableWidgetItem("до морского порта речным транспортом")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setSpan(2,5,2,1)
        self.setItem(2,5,item)

        item = QTableWidgetItem("до морского порта назначения")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setSpan(2,6,2,1)
        self.setItem(2,6,item)

        item = QTableWidgetItem("по железной дороге( I маршрут )")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setSpan(2,7,2,1)
        self.setItem(2,7,item)

        item = QTableWidgetItem("водным транспором(II маршрут)")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setSpan(2,8,2,1)
        self.setItem(2,8,item)

        item = QTableWidgetItem("Объем реализации")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(4,0,item)

        item = QTableWidgetItem("Расстояния")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(5,0,item)

        item = QTableWidgetItem("Объём грузоперевозок")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(6,0,item)

        item = QTableWidgetItem("Тарифы за: 1 т.груза")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(7,0,item)

        item = QTableWidgetItem(" 1 км расстояния")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(8,0,item)

        item = QTableWidgetItem("Стоимость транспорти-ровки по: объёму")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(9,0,item)

        item = QTableWidgetItem("расстоянию")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(10,0,item)

        item = QTableWidgetItem("Всего")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(11,0,item)

        item = QTableWidgetItem(" 1 т.км  грузоперевозок")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(12,0,item)

        item = QTableWidgetItem("затраты  по охране и сопровождению, 5%")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(13,0,item)

        item = QTableWidgetItem("прочие по оформлению, 4%")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(14,0,item)

        item = QTableWidgetItem("прочие организация, 3%")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(15,0,item)

        item = QTableWidgetItem("Всего")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(16,0,item)

        item = QTableWidgetItem("Транспортные расходы на 1 т груза")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(17,0,item)

        item = QTableWidgetItem("Расходы, связанные с реализацией на 1 т груза ")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(18,0,item)

        item = QTableWidgetItem("Всего транспортных и связанных с реализацией расходов на т груза")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(19,0,item)



        # Данные для таблицы (можно заменить на свои)
        data = tabel3

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
    window = TableWindowM(model_test.tab3)
    window.show()
    sys.exit(app.exec())