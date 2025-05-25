import math
from io import StringIO

import pandas as pd
from PyQt6.QtWidgets import QFileDialog, QMainWindow, QWidget, QVBoxLayout, QPushButton

from IU.default_screen import DefaultScreen
from IU.new_model_screen import NewModelScreen
from IU.view_model import ViewModel
from data_tab import Model


class MainScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Модель")
        self.setGeometry(100, 100, 300, 200)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Создаем кнопки
        self.button_new = QPushButton("Новая модель")
        self.button_default = QPushButton("Загрузить модель по умолчанию")
        self.button3 = QPushButton("Загрузить модель")

        # Добавляем кнопки в layout
        layout.addWidget(self.button_new)
        layout.addWidget(self.button_default)
        layout.addWidget(self.button3)

        # Подключаем обработчики нажатий
        self.button_new.clicked.connect(self.on_button_new_click)
        self.button_default.clicked.connect(self.on_button_default_click)
        self.button3.clicked.connect(self.on_button3_click)

    def on_button_default_click(self):
        self.second_window = DefaultScreen()
        self.second_window.show()
        print("Загрузить модель по умолчанию")

    def on_button_new_click(self):
        self.second_window = NewModelScreen()
        self.second_window.show()
        print("Новая модель")

    def on_button3_click(self):
        """Обработчик для загрузки модели из .cxo"""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Выберите файл модели",
            "",
            "*.cxo"
        )
        if not file_path:
            return  # Пользователь отменил выбор

        try:
            model = self.load_model_from_cxo(file_path)
            self.second_window = ViewModel(model)
            self.second_window.show()
        except Exception as e:
            from PyQt6.QtWidgets import QMessageBox
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить файл:\n{str(e)}")


    def load_model_from_cxo(self, file_path):
        """
        Читает .cxo файл и создаёт модель с данными.
        Все значения, которые можно привести к числу — конвертируются в float,
        остальные заменяются на пустую строку.
        """
        model = Model()

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        sections = {}
        current_section = None
        lines = content.splitlines()

        for line in lines:
            line = line.strip()
            if line.startswith("[") and line.endswith("]"):
                current_section = line[1:-1]
                sections[current_section] = []
            elif current_section:
                sections[current_section].append(line)

        for section_name, csv_lines in sections.items():
            if not csv_lines:
                continue

            # Парсим CSV
            df = pd.read_csv(StringIO("\n".join(csv_lines)))

            # Приводим каждую ячейку к float, если возможно, иначе ''
            def safe_convert(value):
                try:
                    num = float(value)
                    if math.isnan(num):
                        return ""
                    return num
                except (ValueError, TypeError):
                    return ""

            # Применяем преобразование ко всей таблице
            df = df.map(safe_convert)

            # Сохраняем в модель
            if hasattr(model, section_name):
                setattr(model, section_name, df)

        return model
