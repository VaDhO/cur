from IU.view_model import ViewModel
from data_tab import Model


class DefaultScreen(ViewModel):
    def __init__(self):
        super().__init__(Model())
