import sys

from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton)

from IU.diolog import ModelParametersDialogCXO, ModelParametersDialogPROM, ModelParametersDialogNORM, \
    ModelParametersDialogTrCXO, ModelParametersDialogTrProm
from IU.view_model import ViewModel
from data_tab import Model


class NewModelScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Моделирование системы")
        self.setGeometry(100, 100, 600, 300)

        # Модель данных
        self.model_data = Model()

        # Центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Кнопки
        self.btn_cxo = QPushButton("Ввести исходные данные СХО")
        self.btn_prom = QPushButton("Ввести исходные данные Пром. переработка")
        self.btn_norms = QPushButton("Ввести нормативы")
        self.btn_tr_cxo = QPushButton("Ввести данные о доставке в с/х организациях")
        self.btn_tr_prom = QPushButton("Ввести данные о доставке в промышленных организациях")
        self.btn_run_model = QPushButton("Рассчитать модель и показать результаты")

        # Подключаем сигналы
        self.btn_cxo.clicked.connect(self.show_dialog_cxo)
        self.btn_prom.clicked.connect(self.show_dialog_prom)
        self.btn_norms.clicked.connect(self.show_dialog_norms)
        self.btn_tr_cxo.clicked.connect(self.show_dialog_tr_cxo)
        self.btn_tr_prom.clicked.connect(self.show_dialog_tr_prom)
        self.btn_run_model.clicked.connect(self.run_model)

        # Отключение последней кнопки до ввода всех данных
        self.btn_run_model.setEnabled(False)

        # Добавляем кнопки на форму
        layout.addWidget(self.btn_cxo)
        layout.addWidget(self.btn_prom)
        layout.addWidget(self.btn_norms)
        layout.addWidget(self.btn_tr_cxo)
        layout.addWidget(self.btn_tr_prom)
        layout.addWidget(self.btn_run_model)

        # Флаги для проверки ввода данных
        self.data_entered = {
            'cxo': False,
            'prom': False,
            'norms': False,
            'tr_cxo': False,
            'tr_prom': False,
        }

    def show_dialog_cxo(self):
        dialog = ModelParametersDialogCXO(self)
        if dialog.exec() == dialog.DialogCode.Accepted:
            params = dialog.get_parameters()

            def safe_float(value):
                try:
                    return float(value) if value not in (None, '') else 0.0
                except ValueError:
                    return 0.0

            # Запись параметров в модель
            self.model_data.tab1.loc[0, 'СХО'] = safe_float(params[0])
            self.model_data.tab1.loc[1, 'СХО'] = safe_float(params[1])
            self.model_data.tab1.loc[3, 'СХО'] = safe_float(params[2])
            self.model_data.tab1.loc[5, 'СХО'] = safe_float(params[3])
            self.model_data.tab1.loc[7, 'СХО'] = safe_float(params[4])
            self.model_data.tab1.loc[11, 'СХО'] = safe_float(params[5])
            self.model_data.tab1.loc[17, 'СХО'] = safe_float(params[6])
            self.model_data.tab1.loc[22, 'СХО'] = safe_float(params[7])
            self.model_data.tab1.loc[23, 'СХО'] = safe_float(params[8])
            self.model_data.tab1.loc[26, 'СХО'] = safe_float(params[9])
            self.model_data.tab1.loc[27, 'СХО'] = safe_float(params[10])
            self.model_data.tab1.loc[28, 'СХО'] = safe_float(params[11])
            self.model_data.tab1.loc[29, 'СХО'] = safe_float(params[12])

            self.data_entered['cxo'] = True
            self.check_all_data_entered()

    def show_dialog_prom(self):
        dialog = ModelParametersDialogPROM(self)
        if dialog.exec() == dialog.DialogCode.Accepted:
            params = dialog.get_parameters()

            def safe_float(value):
                try:
                    return float(value) if value not in (None, '') else 0.0
                except ValueError:
                    return 0.0

            # Здесь примерное место для записи данных в модель
            # Например:
            self.model_data.tab1.loc[11, 'ПП'] = safe_float(params[0])
            self.model_data.tab1.loc[13, 'ПП'] = safe_float(params[1])
            self.model_data.tab1.loc[22, 'ПП'] = safe_float(params[2])
            self.model_data.tab1.loc[27, 'ПП'] = safe_float(params[3])
            self.model_data.tab1.loc[28, 'ПП'] = safe_float(params[4])

            self.data_entered['prom'] = True
            self.check_all_data_entered()

    def show_dialog_norms(self):
        dialog = ModelParametersDialogNORM(self)
        if dialog.exec() == dialog.DialogCode.Accepted:
            params = dialog.get_parameters()

            def safe_float(value):
                try:
                    return float(value) if value not in (None, '') else 0.0
                except ValueError:
                    return 0.0

            # Здесь место для записи данных в модель
            self.model_data.tab1.loc[13, 'Нормативы'] = safe_float(params[0])
            self.model_data.tab1.loc[26, 'Нормативы'] = safe_float(params[1])
            self.model_data.tab1.loc[27, 'Нормативы'] = safe_float(params[2])

            self.data_entered['norms'] = True
            self.check_all_data_entered()

    def show_dialog_tr_cxo(self):
        dialog = ModelParametersDialogTrCXO(self)
        if dialog.exec() == dialog.DialogCode.Accepted:
            params = dialog.get_parameters()

            def safe_float(value):
                try:
                    return float(value) if value not in (None, '') else 0.0
                except ValueError:
                    return 0.0

            # Запись параметров в модель
            self.model_data.tab3.loc[0, 'ЭФиДГ1Э'] = safe_float(params[0])
            self.model_data.tab3.loc[0, 'ЭФиДГ1П'] = safe_float(params[0])

            self.model_data.tab3.loc[1, 'ЭФиДГ1Э'] = safe_float(params[1])
            self.model_data.tab3.loc[3, 'ЭФиДГ1Э'] = safe_float(params[2])
            self.model_data.tab3.loc[4, 'ЭФиДГ1Э'] = safe_float(params[3])

            self.model_data.tab3.loc[1, 'ЭФиДГ1П'] = safe_float(params[4])
            self.model_data.tab3.loc[3, 'ЭФиДГ1П'] = safe_float(params[5])
            self.model_data.tab3.loc[4, 'ЭФиДГ1П'] = safe_float(params[6])

            self.model_data.tab3.loc[0, 'ЭФиДГ2РП'] = safe_float(params[7])
            self.model_data.tab3.loc[0, 'ЭФиДГ2МП'] = safe_float(params[7])
            self.model_data.tab3.loc[0, 'ЭФиДГ2МПН'] = safe_float(params[7])

            self.model_data.tab3.loc[1, 'ЭФиДГ2РП'] = safe_float(params[8])
            self.model_data.tab3.loc[3, 'ЭФиДГ2РП'] = safe_float(params[9])
            self.model_data.tab3.loc[4, 'ЭФиДГ2РП'] = safe_float(params[10])

            self.model_data.tab3.loc[1, 'ЭФиДГ2МП'] = safe_float(params[11])
            self.model_data.tab3.loc[3, 'ЭФиДГ2МП'] = safe_float(params[12])
            self.model_data.tab3.loc[4, 'ЭФиДГ2МП'] = safe_float(params[13])

            self.model_data.tab3.loc[1, 'ЭФиДГ2МПН'] = safe_float(params[14])
            self.model_data.tab3.loc[3, 'ЭФиДГ2МПН'] = safe_float(params[15])
            self.model_data.tab3.loc[4, 'ЭФиДГ2МПН'] = safe_float(params[16])

            self.data_entered['tr_cxo'] = True
            self.check_all_data_entered()

    def show_dialog_tr_prom(self):
        dialog = ModelParametersDialogTrProm(self)
        if dialog.exec() == dialog.DialogCode.Accepted:
            params = dialog.get_parameters()

            def safe_float(value):
                try:
                    return float(value) if value not in (None, '') else 0.0
                except ValueError:
                    return 0.0

            # Запись параметров в модель
            self.model_data.tab4.loc[0, 'ЭФиДГ1Э'] = safe_float(params[0])
            self.model_data.tab4.loc[0, 'ЭФиДГ1П'] = safe_float(params[0])

            self.model_data.tab4.loc[1, 'ЭФиДГ1Э'] = safe_float(params[1])
            self.model_data.tab4.loc[3, 'ЭФиДГ1Э'] = safe_float(params[2])
            self.model_data.tab4.loc[4, 'ЭФиДГ1Э'] = safe_float(params[3])

            self.model_data.tab4.loc[1, 'ЭФиДГ1П'] = safe_float(params[4])
            self.model_data.tab4.loc[3, 'ЭФиДГ1П'] = safe_float(params[5])
            self.model_data.tab4.loc[4, 'ЭФиДГ1П'] = safe_float(params[6])

            self.model_data.tab4.loc[0, 'ЭФиДГ2РП'] = safe_float(params[7])
            self.model_data.tab4.loc[0, 'ЭФиДГ2МП'] = safe_float(params[7])
            self.model_data.tab4.loc[0, 'ЭФиДГ2МПН'] = safe_float(params[7])

            self.model_data.tab4.loc[1, 'ЭФиДГ2РП'] = safe_float(params[8])
            self.model_data.tab4.loc[3, 'ЭФиДГ2РП'] = safe_float(params[9])
            self.model_data.tab4.loc[4, 'ЭФиДГ2РП'] = safe_float(params[10])

            self.model_data.tab4.loc[1, 'ЭФиДГ2МП'] = safe_float(params[11])
            self.model_data.tab4.loc[3, 'ЭФиДГ2МП'] = safe_float(params[12])
            self.model_data.tab4.loc[4, 'ЭФиДГ2МП'] = safe_float(params[13])

            self.model_data.tab4.loc[1, 'ЭФиДГ2МПН'] = safe_float(params[14])
            self.model_data.tab4.loc[3, 'ЭФиДГ2МПН'] = safe_float(params[15])
            self.model_data.tab4.loc[4, 'ЭФиДГ2МПН'] = safe_float(params[16])

            self.data_entered['tr_prom'] = True
            self.check_all_data_entered()

    def check_all_data_entered(self):
        """Проверяет, все ли данные введены"""
        if all(self.data_entered.values()):
            self.btn_run_model.setEnabled(True)

    def run_model(self):
        """Вызывается после ввода всех данных"""
        self.model_data.calculate_model()  # Выполняем расчет модели

        # Открываем окно с таблицами
        self.results_window = ViewModel(self.model_data)
        self.results_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NewModelScreen()
    window.show()
    sys.exit(app.exec())
