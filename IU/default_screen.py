import sys

from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QApplication

from IU.view_model import WievModel
from data_tab import Model


class DefaultScreen(WievModel):
    def __init__(self):
        super().__init__(Model())