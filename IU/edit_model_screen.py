import sys

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QLineEdit, QPushButton, QFormLayout, QDialog)

from IU.diolog import ModelParametersDialogCXO, ModelParametersDialogPROM, ModelParametersDialogNORM, \
    ModelParametersDialogTrCXO, ModelParametersDialogTrProm
from data_tab import Model


class EditModelScreen(QDialog):
    def __init__(self, model, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Редактирование параметров модели")
        self.setGeometry(100, 100, 600, 300)

        # Модель данных
        self.model_data = model
        self.parent = parent

        # Центральный виджет
        layout = QVBoxLayout(self)

        # Кнопки
        self.btn_cxo = QPushButton("Редактировать исходные данные СХО")
        self.btn_prom = QPushButton("Редактировать исходные данные Пром. переработка")
        self.btn_norms = QPushButton("Редактировать нормативы")
        self.btn_tr_cxo = QPushButton("Редактировать данные о доставке в с/х организациях")
        self.btn_tr_prom = QPushButton("Редактировать данные о доставке в промышленных организациях")
        self.btn_finish = QPushButton("Завершить редактирование")

        # Подключаем сигналы
        self.btn_cxo.clicked.connect(self.show_dialog_cxo)
        self.btn_prom.clicked.connect(self.show_dialog_prom)
        self.btn_norms.clicked.connect(self.show_dialog_norms)
        self.btn_tr_cxo.clicked.connect(self.show_dialog_tr_cxo)
        self.btn_tr_prom.clicked.connect(self.show_dialog_tr_prom)
        self.btn_finish.clicked.connect(self.accept)

        # Добавляем кнопки на форму
        layout.addWidget(self.btn_cxo)
        layout.addWidget(self.btn_prom)
        layout.addWidget(self.btn_norms)
        layout.addWidget(self.btn_tr_cxo)
        layout.addWidget(self.btn_tr_prom)
        layout.addWidget(self.btn_finish)

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
            self.model_data.tab1.loc[0, 'СХО'] = safe_float(params[0]) if params[0] not in (None, '') else \
            self.model_data.tab1.loc[0, 'СХО']
            self.model_data.tab1.loc[1, 'СХО'] = safe_float(params[1]) if params[1] not in (None, '') else \
            self.model_data.tab1.loc[1, 'СХО']
            self.model_data.tab1.loc[3, 'СХО'] = safe_float(params[2]) if params[2] not in (None, '') else \
            self.model_data.tab1.loc[3, 'СХО']
            self.model_data.tab1.loc[5, 'СХО'] = safe_float(params[3]) if params[3] not in (None, '') else \
            self.model_data.tab1.loc[5, 'СХО']
            self.model_data.tab1.loc[7, 'СХО'] = safe_float(params[4]) if params[4] not in (None, '') else \
            self.model_data.tab1.loc[7, 'СХО']
            self.model_data.tab1.loc[11, 'СХО'] = safe_float(params[5]) if params[5] not in (None, '') else \
            self.model_data.tab1.loc[11, 'СХО']
            self.model_data.tab1.loc[17, 'СХО'] = safe_float(params[6]) if params[6] not in (None, '') else \
            self.model_data.tab1.loc[17, 'СХО']
            self.model_data.tab1.loc[22, 'СХО'] = safe_float(params[7]) if params[7] not in (None, '') else \
            self.model_data.tab1.loc[22, 'СХО']
            self.model_data.tab1.loc[23, 'СХО'] = safe_float(params[8]) if params[8] not in (None, '') else \
            self.model_data.tab1.loc[23, 'СХО']
            self.model_data.tab1.loc[26, 'СХО'] = safe_float(params[9]) if params[9] not in (None, '') else \
            self.model_data.tab1.loc[26, 'СХО']
            self.model_data.tab1.loc[27, 'СХО'] = safe_float(params[10]) if params[10] not in (None, '') else \
            self.model_data.tab1.loc[27, 'СХО']
            self.model_data.tab1.loc[28, 'СХО'] = safe_float(params[11]) if params[11] not in (None, '') else \
            self.model_data.tab1.loc[28, 'СХО']
            self.model_data.tab1.loc[29, 'СХО'] = safe_float(params[12]) if params[12] not in (None, '') else \
            self.model_data.tab1.loc[29, 'СХО']

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
            self.model_data.tab1.loc[11, 'ПП'] = safe_float(params[0]) if params[0] not in (None, '') else \
            self.model_data.tab1.loc[11, 'ПП']
            self.model_data.tab1.loc[13, 'ПП'] = safe_float(params[1]) if params[1] not in (None, '') else \
            self.model_data.tab1.loc[13, 'ПП']
            self.model_data.tab1.loc[22, 'ПП'] = safe_float(params[2]) if params[2] not in (None, '') else \
            self.model_data.tab1.loc[22, 'ПП']
            self.model_data.tab1.loc[27, 'ПП'] = safe_float(params[3]) if params[3] not in (None, '') else \
            self.model_data.tab1.loc[27, 'ПП']
            self.model_data.tab1.loc[28, 'ПП'] = safe_float(params[4]) if params[4] not in (None, '') else \
            self.model_data.tab1.loc[28, 'ПП']

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
            self.model_data.tab1.loc[13, 'Нормативы'] = safe_float(params[0]) if params[0] not in (None, '') else self.model_data.tab1.loc[13, 'Нормативы']
            self.model_data.tab1.loc[26, 'Нормативы'] = safe_float(params[1]) if params[0] not in (None, '') else self.model_data.tab1.loc[26, 'Нормативы']
            self.model_data.tab1.loc[27, 'Нормативы'] = safe_float(params[2]) if params[0] not in (None, '') else self.model_data.tab1.loc[27, 'Нормативы']

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
            self.model_data.tab3.loc[0, 'ЭФиДГ1Э'] = safe_float(params[0]) if params[0] not in (None, '') else  self.model_data.tab3.loc[0, 'ЭФиДГ1Э']
            self.model_data.tab3.loc[0, 'ЭФиДГ1П'] = safe_float(params[0]) if params[0] not in (None, '') else  self.model_data.tab3.loc[0, 'ЭФиДГ1П']

            self.model_data.tab3.loc[1, 'ЭФиДГ1Э'] = safe_float(params[1]) if params[1] not in (None, '') else  self.model_data.tab3.loc[1, 'ЭФиДГ1Э']
            self.model_data.tab3.loc[3, 'ЭФиДГ1Э'] = safe_float(params[2]) if params[2] not in (None, '') else  self.model_data.tab3.loc[3, 'ЭФиДГ1Э']
            self.model_data.tab3.loc[4, 'ЭФиДГ1Э'] = safe_float(params[3]) if params[3] not in (None, '') else  self.model_data.tab3.loc[4, 'ЭФиДГ1Э']

            self.model_data.tab3.loc[1, 'ЭФиДГ1П'] = safe_float(params[4]) if params[4] not in (None, '') else  self.model_data.tab3.loc[1, 'ЭФиДГ1П']
            self.model_data.tab3.loc[3, 'ЭФиДГ1П'] = safe_float(params[5]) if params[5] not in (None, '') else  self.model_data.tab3.loc[3, 'ЭФиДГ1П']
            self.model_data.tab3.loc[4, 'ЭФиДГ1П'] = safe_float(params[6]) if params[6] not in (None, '') else  self.model_data.tab3.loc[4, 'ЭФиДГ1П']

            self.model_data.tab3.loc[0, 'ЭФиДГ2РП'] = safe_float(params[7]) if params[7] not in (None, '') else  self.model_data.tab3.loc[0, 'ЭФиДГ2РП']
            self.model_data.tab3.loc[0, 'ЭФиДГ2МП'] = safe_float(params[7]) if params[7] not in (None, '') else  self.model_data.tab3.loc[0, 'ЭФиДГ2МП']
            self.model_data.tab3.loc[0, 'ЭФиДГ2МПН'] = safe_float(params[7]) if params[7] not in (None, '') else  self.model_data.tab3.loc[0, 'ЭФиДГ2МПН']

            self.model_data.tab3.loc[1, 'ЭФиДГ2РП'] = safe_float(params[8]) if params[8] not in (None, '') else  self.model_data.tab3.loc[1, 'ЭФиДГ2РП']
            self.model_data.tab3.loc[3, 'ЭФиДГ2РП'] = safe_float(params[9]) if params[9] not in (None, '') else  self.model_data.tab3.loc[3, 'ЭФиДГ2РП']
            self.model_data.tab3.loc[4, 'ЭФиДГ2РП'] = safe_float(params[10]) if params[10] not in (None, '') else  self.model_data.tab3.loc[4, 'ЭФиДГ2РП']

            self.model_data.tab3.loc[1, 'ЭФиДГ2МП'] = safe_float(params[11]) if params[11] not in (None, '') else  self.model_data.tab3.loc[1, 'ЭФиДГ2МП']
            self.model_data.tab3.loc[3, 'ЭФиДГ2МП'] = safe_float(params[12]) if params[12] not in (None, '') else  self.model_data.tab3.loc[3, 'ЭФиДГ2МП']
            self.model_data.tab3.loc[4, 'ЭФиДГ2МП'] = safe_float(params[13]) if params[13] not in (None, '') else  self.model_data.tab3.loc[4, 'ЭФиДГ2МП']

            self.model_data.tab3.loc[1, 'ЭФиДГ2МПН'] = safe_float(params[14]) if params[14] not in (None, '') else  self.model_data.tab3.loc[1, 'ЭФиДГ2МПН']
            self.model_data.tab3.loc[3, 'ЭФиДГ2МПН'] = safe_float(params[15]) if params[15] not in (None, '') else  self.model_data.tab3.loc[3, 'ЭФиДГ2МПН']
            self.model_data.tab3.loc[4, 'ЭФиДГ2МПН'] = safe_float(params[16]) if params[16] not in (None, '') else  self.model_data.tab3.loc[4, 'ЭФиДГ2МПН']

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
            self.model_data.tab4.loc[0, 'ЭФиДГ1Э'] = safe_float(params[0]) if params[0] not in (None, '') else  self.model_data.tab4.loc[0, 'ЭФиДГ1Э']
            self.model_data.tab4.loc[0, 'ЭФиДГ1П'] = safe_float(params[0]) if params[0] not in (None, '') else  self.model_data.tab4.loc[0, 'ЭФиДГ1П']

            self.model_data.tab4.loc[1, 'ЭФиДГ1Э'] = safe_float(params[1]) if params[1] not in (None, '') else  self.model_data.tab4.loc[1, 'ЭФиДГ1Э']
            self.model_data.tab4.loc[3, 'ЭФиДГ1Э'] = safe_float(params[2]) if params[2] not in (None, '') else  self.model_data.tab4.loc[3, 'ЭФиДГ1Э']
            self.model_data.tab4.loc[4, 'ЭФиДГ1Э'] = safe_float(params[3]) if params[3] not in (None, '') else  self.model_data.tab4.loc[4, 'ЭФиДГ1Э']

            self.model_data.tab4.loc[1, 'ЭФиДГ1П'] = safe_float(params[4]) if params[4] not in (None, '') else  self.model_data.tab4.loc[1, 'ЭФиДГ1П']
            self.model_data.tab4.loc[3, 'ЭФиДГ1П'] = safe_float(params[5]) if params[5] not in (None, '') else  self.model_data.tab4.loc[3, 'ЭФиДГ1П']
            self.model_data.tab4.loc[4, 'ЭФиДГ1П'] = safe_float(params[6]) if params[6] not in (None, '') else  self.model_data.tab4.loc[4, 'ЭФиДГ1П']

            self.model_data.tab4.loc[0, 'ЭФиДГ2РП'] = safe_float(params[7]) if params[7] not in (None, '') else  self.model_data.tab4.loc[0, 'ЭФиДГ2РП']
            self.model_data.tab4.loc[0, 'ЭФиДГ2МП'] = safe_float(params[7]) if params[7] not in (None, '') else  self.model_data.tab4.loc[0, 'ЭФиДГ2МП']
            self.model_data.tab4.loc[0, 'ЭФиДГ2МПН'] = safe_float(params[7]) if params[7] not in (None, '') else  self.model_data.tab4.loc[0, 'ЭФиДГ2МПН']

            self.model_data.tab4.loc[1, 'ЭФиДГ2РП'] = safe_float(params[8]) if params[8] not in (None, '') else  self.model_data.tab4.loc[1, 'ЭФиДГ2РП']
            self.model_data.tab4.loc[3, 'ЭФиДГ2РП'] = safe_float(params[9]) if params[9] not in (None, '') else  self.model_data.tab4.loc[3, 'ЭФиДГ2РП']
            self.model_data.tab4.loc[4, 'ЭФиДГ2РП'] = safe_float(params[10]) if params[10] not in (None, '') else  self.model_data.tab4.loc[4, 'ЭФиДГ2РП']

            self.model_data.tab4.loc[1, 'ЭФиДГ2МП'] = safe_float(params[11]) if params[11] not in (None, '') else  self.model_data.tab4.loc[1, 'ЭФиДГ2МП']
            self.model_data.tab4.loc[3, 'ЭФиДГ2МП'] = safe_float(params[12]) if params[12] not in (None, '') else  self.model_data.tab4.loc[3, 'ЭФиДГ2МП']
            self.model_data.tab4.loc[4, 'ЭФиДГ2МП'] = safe_float(params[13]) if params[13] not in (None, '') else  self.model_data.tab4.loc[4, 'ЭФиДГ2МП']

            self.model_data.tab4.loc[1, 'ЭФиДГ2МПН'] = safe_float(params[14]) if params[14] not in (None, '') else  self.model_data.tab4.loc[1, 'ЭФиДГ2МПН']
            self.model_data.tab4.loc[3, 'ЭФиДГ2МПН'] = safe_float(params[15]) if params[15] not in (None, '') else  self.model_data.tab4.loc[3, 'ЭФиДГ2МПН']
            self.model_data.tab4.loc[4, 'ЭФиДГ2МПН'] = safe_float(params[16]) if params[16] not in (None, '') else  self.model_data.tab4.loc[4, 'ЭФиДГ2МПН']
