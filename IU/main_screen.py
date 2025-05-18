from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton

from IU.default_screen import DefaultScreen
from IU.new_model_screen import NewModelScreen


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


        # Методы-обработчики

    def on_button_default_click(self):
        self.second_window = DefaultScreen()
        self.second_window.show()  # Показываем без блокировки главного
        print("Загрузить модель по умолчанию")

    def on_button_new_click(self):
        self.second_window = NewModelScreen()
        self.second_window.show()
        print("Новая модель")

    def on_button3_click(self):
        print("Загрузить модель")
