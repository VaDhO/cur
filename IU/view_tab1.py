import sys

import pandas as pd
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QMainWindow, QApplication

from data_tab import Model


class ViewTable1(QTableWidget):
    tabel1 = pd.DataFrame()

    def __init__(self, tabel1):
        super().__init__()

        self.setRowCount(45)  # 4 строки
        self.setColumnCount(20)  # 3 столбца

        item = QTableWidgetItem("Показатели")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setSpan(0, 0, 4, 1)
        self.setItem(0, 0, item)

        item = QTableWidgetItem("Исходные данные СХО")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setSpan(0, 1, 4, 1)
        self.setItem(0, 1, item)

        item = QTableWidgetItem("Исходные данные пром")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setSpan(0, 2, 4, 1)
        self.setItem(0, 2, item)

        item = QTableWidgetItem("Нормативы")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setSpan(0, 3, 4, 1)
        self.setItem(0, 3, item)

        item = QTableWidgetItem("Варианты реализации продукции")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setSpan(0, 4, 1, 8)
        self.setItem(0, 4, item)

        item = QTableWidgetItem("маслосемян")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setSpan(1, 4, 1, 2)
        self.setItem(1, 4, item)

        item = QTableWidgetItem("масла подсолнечного")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setSpan(1, 6, 1, 6)
        self.setItem(1, 6, item)

        item = QTableWidgetItem("внутренний рынок")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setSpan(2, 4, 2, 1)
        self.setItem(2, 4, item)

        item = QTableWidgetItem("экспорт")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setSpan(2, 5, 2, 1)
        self.setItem(2, 5, item)

        item = QTableWidgetItem("собственная переработка")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setSpan(2, 6, 1, 4)
        self.setItem(2, 6, item)

        item = QTableWidgetItem("промышленная переработка")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setSpan(2, 10, 1, 2)
        self.setItem(2, 10, item)

        item = QTableWidgetItem("для собственных нужд")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setSpan(3, 6, 1, 1)
        self.setItem(3, 6, item)

        item = QTableWidgetItem("оплата услуг по переработке давальческого сырья")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setSpan(3, 7, 1, 1)
        self.setItem(3, 7, item)

        item = QTableWidgetItem("внутренний рынок")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setSpan(3, 8, 1, 1)
        self.setItem(3, 8, item)

        item = QTableWidgetItem("экспорт")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setSpan(3, 9, 1, 1)
        self.setItem(3, 9, item)

        item = QTableWidgetItem("внутренний рынок")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setSpan(3, 10, 1, 1)
        self.setItem(3, 10, item)

        item = QTableWidgetItem("экспорт")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setSpan(3, 11, 1, 1)
        self.setItem(3, 11, item)

        item = QTableWidgetItem("Итого в том числе:")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setSpan(0, 12, 2, 8)
        self.setItem(0, 12, item)

        item = QTableWidgetItem("маслосемена")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setSpan(2, 12, 2, 1)
        self.setItem(2, 12, item)

        item = QTableWidgetItem("масло подсолнечное")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setSpan(2, 13, 1, 4)
        self.setItem(2, 13, item)

        item = QTableWidgetItem("собственная переработка")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setSpan(3, 13, 1, 1)
        self.setItem(3, 13, item)

        item = QTableWidgetItem("промышленная переработка")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setSpan(3, 14, 1, 1)
        self.setItem(3, 14, item)

        item = QTableWidgetItem("внутренний рынок")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setSpan(3, 15, 1, 1)
        self.setItem(3, 15, item)

        item = QTableWidgetItem("экспорт")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setSpan(3, 16, 1, 1)
        self.setItem(3, 16, item)

        item = QTableWidgetItem("Всего масло подсолнеч-ное")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setSpan(2, 17, 2, 1)
        self.setItem(2, 17, item)

        item = QTableWidgetItem("Итого маслосемена и масло под-солнечное")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setSpan(2, 18, 2, 1)
        self.setItem(2, 18, item)

        item = QTableWidgetItem("в том числе сельское хозяйство")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setSpan(2, 19, 2, 1)
        self.setItem(2, 19, item)

        item = QTableWidgetItem("Посевная площадь, га")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(4, 0, item)

        item = QTableWidgetItem("Урожайность, ц/га")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(5, 0, item)

        item = QTableWidgetItem("Выход и распределение продукции всего, ц")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(6, 0, item)

        item = QTableWidgetItem("Себестоимость 1 ц, руб.")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(7, 0, item)

        item = QTableWidgetItem("Себестоимость всего, тыс.руб")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(8, 0, item)

        item = QTableWidgetItem(
            "Направлено на переработку и реализацию маслосемян: корректирующий коэффициент выхода сырья, ед. ")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(9, 0, item)

        item = QTableWidgetItem("   сумма всего, ц")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(10, 0, item)

        item = QTableWidgetItem("Себестоимость сырья для переработки: корректирующий коэффициент, ед.")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(11, 0, item)

        item = QTableWidgetItem("   1 ц , руб.")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(12, 0, item)

        item = QTableWidgetItem("Стоимость сырья для переработки, тыс.руб.")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(13, 0, item)

        item = QTableWidgetItem("Выход готовой продукции: корректирующий коэффициент выхода из 1 ц маслосемян,ед.")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(14, 0, item)

        item = QTableWidgetItem("   сумма всего, ц")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(15, 0, item)

        item = QTableWidgetItem("Затраты на переработку и доработку маслосемян: корректирующий коэффициент, ед.")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(16, 0, item)

        item = QTableWidgetItem("   сумма всего, тыс.руб.")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(17, 0, item)

        item = QTableWidgetItem("Себестоимость готовой продукции всего, тыс.руб.")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(18, 0, item)

        item = QTableWidgetItem("Себестоимость 1 ц готовой продукции, руб.")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(19, 0, item)

        item = QTableWidgetItem("Товарность: корректирующий коэффициент,ед.")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(20, 0, item)

        item = QTableWidgetItem("Объем реализации, ц")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(21, 0, item)

        item = QTableWidgetItem("Транспортные расходы на реализацию: корректирующий коэффициент, ед.")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(22, 0, item)

        item = QTableWidgetItem("   сумма всего, тыс.руб.")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(23, 0, item)

        item = QTableWidgetItem("Затраты, связанные с реализацией продукции: корректирующий коэффициент, ед.")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(24, 0, item)

        item = QTableWidgetItem("   сумма всего, тыс.руб.")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(25, 0, item)

        item = QTableWidgetItem("    в расчете на 1 ц, руб.")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(26, 0, item)

        item = QTableWidgetItem("Полная себестоимость реализованной продукции, тыс. руб")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(27, 0, item)

        item = QTableWidgetItem("Полная себестоимость 1 ц реализованной продукции, руб.")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(28, 0, item)

        item = QTableWidgetItem("Средняя цена единицы продукции: корректирующий коэффициент, ед.")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(29, 0, item)

        item = QTableWidgetItem("    маслосемян, руб.")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(30, 0, item)

        item = QTableWidgetItem("   масла подсолнечного, руб.")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(31, 0, item)

        item = QTableWidgetItem("Таможенная пошлина, руб.")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(32, 0, item)

        item = QTableWidgetItem("Цена без пошлины, руб./ц")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(33, 0, item)

        item = QTableWidgetItem("Выручка от реализации продукции, тыс.руб.: маслосемян с пошлиной")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(34, 0, item)

        item = QTableWidgetItem("   без пошлины")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(35, 0, item)

        item = QTableWidgetItem("   масла подсолнечного с пошлиной")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(36, 0, item)

        item = QTableWidgetItem("   без пошлины")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(37, 0, item)

        item = QTableWidgetItem("Прибыль продаж, тыс.руб.:с пошлиной")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(38, 0, item)

        item = QTableWidgetItem("   без пошлины")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(39, 0, item)

        item = QTableWidgetItem("Рентабельность продаж,%:с пошлиной")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(40, 0, item)

        item = QTableWidgetItem("   без пошлины")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(41, 0, item)

        item = QTableWidgetItem("Пошлина, тыс.руб.")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(42, 0, item)

        item = QTableWidgetItem("Доля в полной прибыли, %")
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        self.setItem(43, 0, item)

        # Данные для таблицы (можно заменить на свои)
        data = tabel1

        # Заполняем таблицу
        for row_idx, row_data in enumerate(list(data.columns)):
            for col_idx, cell_data in enumerate(data[row_data]):
                if type(cell_data) == float:
                    item = QTableWidgetItem("{:.2f}".format(float(cell_data)))
                    item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)  # Запрет редактирования
                else:
                    item = QTableWidgetItem(cell_data)
                    item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)  # Запрет редактирования
                self.setItem(col_idx + 4, row_idx + 1, item)

    def update_data(self, data):
        self.setRowCount(len(data))
        for row_idx, row_data in enumerate(data.values):
            for col_idx, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
                self.setItem(row_idx, col_idx, item)
