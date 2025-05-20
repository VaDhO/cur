import sys

import pandas as pd
from PyQt6.QtWidgets import (QTabWidget, QMainWindow, QWidget, QVBoxLayout,
                             QApplication, QPushButton, QHBoxLayout, QMessageBox, QFileDialog)

from IU.View_tab6 import ViewTable6
from IU.view_tab1 import ViewTable1
from IU.view_tab3 import ViewTable3
from IU.view_tab5 import ViewTable5
from data_tab import Model
from defa import save_all_tables_to_excel_with_headers


class ViewModel(QMainWindow):
    def __init__(self, model_new):
        super().__init__()
        self.setWindowTitle("Приложение с вкладками")
        self.setGeometry(100, 100, 1000, 700)
        self.model = model_new

        # Главный контейнер
        main_widget = QWidget()
        main_layout = QVBoxLayout(main_widget)
        self.setCentralWidget(main_widget)

        # --- Блок кнопок сверху ---
        top_button_layout = QHBoxLayout()

        # Кнопка "Рассчитать"
        self.calculate_btn = QPushButton("Рассчитать")
        self.calculate_btn.clicked.connect(self.calculate_and_update)
        self.calculate_btn.setFixedHeight(40)

        # Кнопка "Сохранить в Excel"
        self.save_excel_btn = QPushButton("Сохранить всё в Excel")
        self.save_excel_btn.clicked.connect(self.save_full_model_to_excel)
        self.save_excel_btn.setFixedHeight(40)

        # Кнопка "Сохранить в .cxo"
        self.save_cxo_btn = QPushButton("Сохранить всё в .cxo")
        self.save_cxo_btn.clicked.connect(self.save_to_cxo)
        self.save_cxo_btn.setFixedHeight(40)

        # Стили для кнопок
        button_style = """
            QPushButton {
                background-color: #2196F3;
                color: white;
                font-weight: bold;
                border: none;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
        """
        self.calculate_btn.setStyleSheet(button_style)
        self.save_excel_btn.setStyleSheet(button_style)
        self.save_cxo_btn.setStyleSheet(button_style)

        # Добавляем кнопки в layout
        top_button_layout.addWidget(self.calculate_btn)
        top_button_layout.addWidget(self.save_excel_btn)
        top_button_layout.addWidget(self.save_cxo_btn)

        # --- Вкладки ---
        self.tabs = QTabWidget()

        # --- Добавляем всё в основной layout ---
        main_layout.addLayout(top_button_layout)
        main_layout.addWidget(self.tabs)

        # Инициализация вкладок
        self.init_tabs()

    def init_tabs(self):
        """Инициализация всех вкладок с текущими данными модели"""
        while self.tabs.count() > 0:
            self.tabs.removeTab(0)

        self.add_table_tab(ViewTable1(self.model.tab1), "Модель последняя")
        self.add_table_tab(ViewTable3(self.model.tab3), "Затраты по маслу в сх")
        self.add_table_tab(ViewTable3(self.model.tab4), "Затраты по маслу в пр")
        self.add_table_tab(ViewTable5(self.model.tab5), "Регулирующий блок")
        self.add_table_tab(ViewTable6(self.model.tab6), "Управляющий блок")

    def add_table_tab(self, widget, title):
        layout = QVBoxLayout()
        layout.addWidget(widget)
        container = QWidget()
        container.setLayout(layout)
        self.tabs.addTab(container, title)

    def calculate_and_update(self):
        try:
            self.model.calculate_model()
            self.init_tabs()
            QMessageBox.information(self, "Успех", "Модель успешно рассчитана!")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка при расчете модели:\n{str(e)}")

    def save_to_excel(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Сохранить в Excel", "", "*.xlsx")
        if not file_path:
            return

        try:
            with pd.ExcelWriter(file_path) as writer:
                self.model.tab1.to_excel(writer, sheet_name='Модель последняя', index=False)
                self.model.tab3.to_excel(writer, sheet_name='Затраты по маслу в сх', index=False)
                self.model.tab4.to_excel(writer, sheet_name='Затраты по маслу в пр', index=False)
                self.model.tab5.to_excel(writer, sheet_name='Регулирующий блок', index=False)
                self.model.tab6.to_excel(writer, sheet_name='Управляющий блок', index=False)
            QMessageBox.information(self, "Успех", f"Данные успешно сохранены в Excel:\n{file_path}")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить файл:\n{str(e)}")

    def save_to_cxo(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Сохранить в .cxo", "", "*.cxo")
        if not file_path:
            return

        try:
            # Пример: сохраняем все таблицы как CSV, разделенные секциями
            with open(file_path, 'w', encoding='utf-8') as f:
                for name, df in [
                    ('tab1', self.model.tab1),
                    ('tab3', self.model.tab3),
                    ('tab4', self.model.tab4),
                    ('tab5', self.model.tab5),
                    ('tab6', self.model.tab6)
                ]:
                    f.write(f"[{name}]\n")
                    df.to_csv(f, index=False)
            QMessageBox.information(self, "Успех", f"Данные успешно сохранены в .cxo:\n{file_path}")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить файл:\n{str(e)}")

    def save_full_model_to_excel(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Сохранить всё в Excel", "", "*.xlsx")
        if not file_path:
            return

        try:
            save_all_tables_to_excel_with_headers(self.tabs, file_path)
            QMessageBox.information(self, "Успех", f"Файл успешно сохранён:\n{file_path}")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить файл:\n{str(e)}")

if __name__ == "__main__":
    model = Model()
    app = QApplication(sys.argv)
    window = ViewModel(model)
    window.show()
    sys.exit(app.exec())