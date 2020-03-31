from PyQt5.QtWidgets import QWidget

from .ui_testsucceed import Ui_Form


class SucceedWidget(QWidget):

    def __init__(self, parent):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
