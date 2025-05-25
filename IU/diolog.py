from PyQt6.QtWidgets import (QVBoxLayout, QHBoxLayout,
                             QLineEdit, QPushButton, QFormLayout, QDialog)


class ModelParametersDialogCXO(QDialog):
    """Диалоговое окно для ввода параметров модели"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Отчет CXO")
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
        form_layout.addRow(
            "Направлено на переработку и реализацию маслосемян: корректирующий коэффициент выхода сырья, ед. ",
            self.param4_input)
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
        self.calculate_btn = QPushButton("Записать")
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
        self.setWindowTitle("Отчет пром.перераб")
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
        self.calculate_btn = QPushButton("Записать")
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
            self.param5_input.text()
        ]


class ModelParametersDialogNORM(QDialog):
    """Диалоговое окно для ввода параметров модели"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Нормативы")
        self.setFixedSize(700, 500)

        layout = QVBoxLayout()
        form_layout = QFormLayout()

        # Поля для параметров
        self.param1_input = QLineEdit()
        self.param2_input = QLineEdit()
        self.param3_input = QLineEdit()

        # Добавляем поля в форму
        form_layout.addRow("Затраты на переработку и доработку маслосемян сумма всего, тыс.руб.", self.param1_input)
        form_layout.addRow("Средняя цена единицы продукции маслосемян, руб.", self.param2_input)
        form_layout.addRow("Средняя цена единицы продукции масла подсолнечного, руб.", self.param3_input)

        # Кнопки
        self.calculate_btn = QPushButton("Записать")
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
            self.param3_input.text()
        ]


class ModelParametersDialogTrCXO(QDialog):
    """Диалоговое окно для ввода параметров модели"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Транспортировка СХ")
        self.setFixedSize(800, 600)

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
        self.param14_input = QLineEdit()
        self.param15_input = QLineEdit()
        self.param16_input = QLineEdit()
        self.param17_input = QLineEdit()

        # Добавляем поля в форму
        form_layout.addRow("Объем реализации I маршрут, т:", self.param1_input)

        form_layout.addRow("Расстояния I маршрут до элеватора автомобильным транспортом, км:", self.param2_input)
        form_layout.addRow("\tТарифы за: 1 т.груза, тыс.руб:", self.param3_input)
        form_layout.addRow("\t\tТарифы за:  1 км расстояния, тыс.руб:", self.param4_input)

        form_layout.addRow("Расстояния I маршрут до пункта назначения по железной дороге, км:", self.param5_input)
        form_layout.addRow("\tТарифы за: 1 т.груза, тыс.руб:", self.param6_input)
        form_layout.addRow("\t\tТарифы за:  1 км расстояния, тыс.руб:", self.param7_input)

        form_layout.addRow("Объем реализации II маршрут, т:", self.param8_input)

        form_layout.addRow("Расстояния II маршрут до речного порта, км:", self.param9_input)
        form_layout.addRow("\tТарифы за: 1 т.груза, тыс.руб:", self.param10_input)
        form_layout.addRow("\t\tТарифы за:  1 км расстояния, тыс.руб:", self.param11_input)

        form_layout.addRow("Расстояния II маршрут до морского порта речным транспортом, км:", self.param12_input)
        form_layout.addRow("\tТарифы за: 1 т.груза, тыс.руб:", self.param13_input)
        form_layout.addRow("\t\tТарифы за:  1 км расстояния, тыс.руб:", self.param14_input)

        form_layout.addRow("Расстояния II маршрут до морского порта назначения, км:", self.param15_input)
        form_layout.addRow("\tТарифы за: 1 т.груза, тыс.руб:", self.param16_input)
        form_layout.addRow("\t\tТарифы за:  1 км расстояния, тыс.руб:", self.param17_input)

        # Кнопки
        self.calculate_btn = QPushButton("Записать")
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
            self.param13_input.text(),
            self.param14_input.text(),
            self.param15_input.text(),
            self.param16_input.text(),
            self.param17_input.text()
        ]


class ModelParametersDialogTrProm(QDialog):
    """Диалоговое окно для ввода параметров модели"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Транспортировка промышленность")
        self.setFixedSize(800, 600)

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
        self.param14_input = QLineEdit()
        self.param15_input = QLineEdit()
        self.param16_input = QLineEdit()
        self.param17_input = QLineEdit()

        # Добавляем поля в форму
        form_layout.addRow("Объем реализации I маршрут, т:", self.param1_input)

        form_layout.addRow("Расстояния I маршрут до элеватора автомобильным транспортом, км:", self.param2_input)
        form_layout.addRow("\tТарифы за: 1 т.груза, тыс.руб:", self.param3_input)
        form_layout.addRow("\t\tТарифы за:  1 км расстояния, тыс.руб:", self.param4_input)

        form_layout.addRow("Расстояния I маршрут до пункта назначения по железной дороге, км:", self.param5_input)
        form_layout.addRow("\tТарифы за: 1 т.груза, тыс.руб:", self.param6_input)
        form_layout.addRow("\t\tТарифы за:  1 км расстояния, тыс.руб:", self.param7_input)

        form_layout.addRow("Объем реализации II маршрут, т:", self.param8_input)

        form_layout.addRow("Расстояния II маршрут до речного порта, км:", self.param9_input)
        form_layout.addRow("\tТарифы за: 1 т.груза, тыс.руб:", self.param10_input)
        form_layout.addRow("\t\tТарифы за:  1 км расстояния, тыс.руб:", self.param11_input)

        form_layout.addRow("Расстояния II маршрут до морского порта речным транспортом, км:", self.param12_input)
        form_layout.addRow("\tТарифы за: 1 т.груза, тыс.руб:", self.param13_input)
        form_layout.addRow("\t\tТарифы за:  1 км расстояния, тыс.руб:", self.param14_input)

        form_layout.addRow("Расстояния II маршрут до морского порта назначения, км:", self.param15_input)
        form_layout.addRow("\tТарифы за: 1 т.груза, тыс.руб:", self.param16_input)
        form_layout.addRow("\t\tТарифы за:  1 км расстояния, тыс.руб:", self.param17_input)

        # Кнопки
        self.calculate_btn = QPushButton("Записать")
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
            self.param13_input.text(),
            self.param14_input.text(),
            self.param15_input.text(),
            self.param16_input.text(),
            self.param17_input.text()
        ]
