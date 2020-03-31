
from PyQt5.QtWidgets import QWidget

from .ui_testFail import Ui_Form


class FailWidget(QWidget):

    def __init__(self, parent):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
