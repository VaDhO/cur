import sys
import pandas as pd
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QTabWidget, QMainWindow, QWidget, QVBoxLayout,
                             QApplication, QTableWidget, QTableWidgetItem,
                             QPushButton, QHBoxLayout, QMessageBox)

from IU.View_tab6 import ViewTable6
from IU.view_tab1 import ViewTable1
from IU.view_tab3 import ViewTable3
from IU.view_tab5 import ViewTable5
from data_tab import Model


class WievModel(QMainWindow):
    def __init__(self, model_new):
        super().__init__()
        self.setWindowTitle("Приложение с вкладками")
        self.setGeometry(100, 100, 800, 600)
        self.model = model_new

        # Главный контейнер с кнопкой и вкладками
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        # Создаем кнопку "Рассчитать"
        self.calculate_btn = QPushButton("Рассчитать")
        self.calculate_btn.clicked.connect(self.calculate_and_update)
        self.calculate_btn.setFixedHeight(40)
        self.calculate_btn.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-weight: bold;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)

        # Контейнер для кнопки (чтобы выровнять по центру)
        btn_container = QWidget()
        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.calculate_btn)
        btn_container.setLayout(btn_layout)

        # Создаем вкладки
        self.tabs = QTabWidget()

        # Добавляем кнопку и вкладки в основной layout
        main_layout.addWidget(btn_container)
        main_layout.addWidget(self.tabs)

        # Инициализируем вкладки
        self.init_tabs()

    def init_tabs(self):
        """Инициализация всех вкладок с текущими данными модели"""
        # Очищаем существующие вкладки
        while self.tabs.count() > 0:
            self.tabs.removeTab(0)

        # Добавляем обновленные вкладки
        self.add_table_tab(ViewTable1(self.model.tab1), "Модель последняя")
        self.add_table_tab(ViewTable3(self.model.tab3), "Затраты по маслу в сх")
        self.add_table_tab(ViewTable3(self.model.tab4), "Затраты по маслу в пр")
        self.add_table_tab(ViewTable5(self.model.tab5), "Регулирующий блок")
        self.add_table_tab(ViewTable6(self.model.tab6), "Управляющий блок")

    def add_table_tab(self, widget, title):
        """Добавляет вкладку с таблицей"""
        layout = QVBoxLayout()
        layout.addWidget(widget)
        container = QWidget()
        container.setLayout(layout)
        self.tabs.addTab(container, title)

    def calculate_and_update(self):
        """Выполняет расчет модели и обновляет все вкладки"""
        try:
            # Вызываем расчет модели
            self.model.calculate_model()

            # Обновляем все вкладки с новыми данными
            self.init_tabs()

            # Уведомление об успешном расчете
            QMessageBox.information(self, "Успех", "Модель успешно рассчитана!")

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка при расчете модели:\n{str(e)}")


if __name__ == "__main__":
    model = Model()
    app = QApplication(sys.argv)
    window = WievModel(model)
    window.show()
    sys.exit(app.exec())