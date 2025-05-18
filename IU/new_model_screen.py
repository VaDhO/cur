import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QPushButton, QTabWidget, QTableWidget,
                             QTableWidgetItem, QMessageBox, QFormLayout, QDialog)
from PyQt6.QtCore import Qt

from IU.view_model import ViewModel
from data_tab import Model


class ModelParametersDialogCXO(QDialog):
    """Диалоговое окно для ввода параметров модели"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Параметры модели")
        self.setFixedSize(700, 500)

        layout = QVBoxLayout()
        form_layout = QFormLayout()

        # Поля для параметров
        self.param1_input = QLineEdit()
        self.param2_input = QLineEdit()
        self.param3_input = QLineEdit()
        self.param4_input = QLineEdit()
        self.param5_input = QLineEdit()
        self.param6_input = QLineEdit()
        self.param7_input = QLineEdit()
        self.param8_input = QLineEdit()
        self.param9_input = QLineEdit()
        self.param10_input = QLineEdit()
        self.param11_input = QLineEdit()
        self.param12_input = QLineEdit()
        self.param13_input = QLineEdit()


        # Добавляем поля в форму
        form_layout.addRow("Посевная площадь, га:", self.param1_input)
        form_layout.addRow("Урожайность, ц/га:", self.param2_input)
        form_layout.addRow("Себестоимость 1 ц, руб.:", self.param3_input)
        form_layout.addRow("Направлено на переработку и реализацию маслосемян: корректирующий коэффициент выхода сырья, ед. ", self.param4_input)
        form_layout.addRow("Себестоимость сырья для переработки: корректирующий коэффициент, ед.", self.param5_input)
        form_layout.addRow("Выход готовой продукции сумма всего, ц", self.param6_input)
        form_layout.addRow("Объем реализации, ц", self.param7_input)
        form_layout.addRow("Затраты, связанные с реализацией продукции в расчете на 1 ц, руб.", self.param8_input)
        form_layout.addRow("Полная себестоимость реализованной продукции, тыс. руб", self.param9_input)
        form_layout.addRow("Средняя цена единицы продукции масла подсолнечного, руб. ", self.param10_input)
        form_layout.addRow("Средняя цена единицы продукции маслосемян, руб.", self.param11_input)
        form_layout.addRow("Таможенная пошлина, руб.", self.param12_input)
        form_layout.addRow("Цена без пошлины, руб./ц", self.param13_input)


        # Кнопки
        self.calculate_btn = QPushButton("Рассчитать")
        self.cancel_btn = QPushButton("Отмена")

        # Расположение кнопок
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.calculate_btn)
        button_layout.addWidget(self.cancel_btn)

        # Собираем все вместе
        layout.addLayout(form_layout)
        layout.addLayout(button_layout)
        self.setLayout(layout)

        # Подключаем сигналы
        self.calculate_btn.clicked.connect(self.accept)
        self.cancel_btn.clicked.connect(self.reject)

    def get_parameters(self):
        """Возвращает введенные параметры"""
        return [
            self.param1_input.text(),
            self.param2_input.text(),
            self.param3_input.text(),
            self.param4_input.text(),
            self.param5_input.text(),
            self.param6_input.text(),
            self.param7_input.text(),
            self.param8_input.text(),
            self.param9_input.text(),
            self.param10_input.text(),
            self.param11_input.text(),
            self.param12_input.text(),
            self.param13_input.text()
        ]


class ModelParametersDialogPROM(QDialog):
    """Диалоговое окно для ввода параметров модели"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Параметры модели")
        self.setFixedSize(700, 500)

        layout = QVBoxLayout()
        form_layout = QFormLayout()

        # Поля для параметров
        self.param1_input = QLineEdit()
        self.param2_input = QLineEdit()
        self.param3_input = QLineEdit()
        self.param4_input = QLineEdit()
        self.param5_input = QLineEdit()


        # Добавляем поля в форму
        form_layout.addRow("Выход готовой продукции сумма всего, ц", self.param1_input)
        form_layout.addRow("Затраты на переработку и доработку маслосемян сумма всего, тыс.руб.", self.param2_input)
        form_layout.addRow("Затраты, связанные с реализацией продукции в расчете на 1 ц, руб.", self.param3_input)
        form_layout.addRow("Средняя цена единицы продукции масла подсолнечного, руб.", self.param4_input)
        form_layout.addRow("Таможенная пошлина, руб.", self.param5_input)

        # Кнопки
        self.calculate_btn = QPushButton("Рассчитать")
        self.cancel_btn = QPushButton("Отмена")

        # Расположение кнопок
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.calculate_btn)
        button_layout.addWidget(self.cancel_btn)

        # Собираем все вместе
        layout.addLayout(form_layout)
        layout.addLayout(button_layout)
        self.setLayout(layout)

        # Подключаем сигналы
        self.calculate_btn.clicked.connect(self.accept)
        self.cancel_btn.clicked.connect(self.reject)

    def get_parameters(self):
        """Возвращает введенные параметры"""
        return [
            self.param1_input.text(),
            self.param2_input.text(),
            self.param3_input.text(),
            self.param4_input.text(),
            self.param5_input.text(),
            self.param6_input.text(),
            self.param7_input.text(),
            self.param8_input.text(),
            self.param9_input.text(),
            self.param10_input.text(),
            self.param11_input.text(),
            self.param12_input.text(),
            self.param13_input.text()
        ]


class NewModelScreen(QMainWindow):
    """Главное окно приложения"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Моделирование системы")
        self.setGeometry(100, 100, 400, 200)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Кнопка запуска моделирования
        self.start_btn = QPushButton("Запустить моделирование")
        self.start_btn.clicked.connect(self.show_parameters_dialog)
        layout.addWidget(self.start_btn)

        # Модель (заглушка)
        self.model_data = Model()

    def show_parameters_dialog(self):
        """Показывает диалог ввода параметров"""
        dialog = ModelParametersDialogCXO(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            params = dialog.get_parameters()
            self.model_data.tab1.loc[0, 'СХО'] = float(params[0])
            self.model_data.tab1.loc[1, 'СХО'] = float(params[1])
            self.model_data.tab1.loc[3, 'СХО'] = float(params[2])
            self.model_data.tab1.loc[5, 'СХО'] = float(params[3])
            self.model_data.tab1.loc[7, 'СХО'] = float(params[4])
            self.model_data.tab1.loc[11, 'СХО'] = float(params[5])
            self.model_data.tab1.loc[17, 'СХО'] = float(params[6])
            self.model_data.tab1.loc[22, 'СХО'] = float(params[7])
            self.model_data.tab1.loc[23, 'СХО'] = float(params[8])
            self.model_data.tab1.loc[26, 'СХО'] = float(params[9])
            self.model_data.tab1.loc[27, 'СХО'] = float(params[10])
            self.model_data.tab1.loc[28, 'СХО'] = float(params[11])
            self.model_data.tab1.loc[29, 'СХО'] = float(params[12])

            #self.model_data.calculate_model()

            # Показываем окно результатов
            self.results_window = ViewModel(self.model_data)
            self.results_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NewModelScreen()
    window.show()
    sys.exit(app.exec())