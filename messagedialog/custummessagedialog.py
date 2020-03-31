
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
from .ui_messagedialog import Ui_MessageDialog


class CustumMessageDialog(QDialog):

    NO = 'no'
    YES = 'yes'
    CANCEL = 'cancel'
    OK = 'OK'

    def __init__(self, parent, message='', windowTitle='', showOk=False, showCancel=False, showYes=False,
                showNo=False):
        super().__init__(parent)

        self.ui = Ui_MessageDialog()
        self.ui.setupUi(self)

        self.ui.label_message.setText(message)
        self.setWindowTitle(windowTitle)
        self._selectedAnswer = 0

        if showCancel:
            self.ui.pushButton_cancel.show()
        else:
            self.ui.pushButton_cancel.hide()

        if showOk:
            self.ui.pushButton_ok.show()
        else:
            self.ui.pushButton_ok.hide()

        if showYes:
            self.ui.pushButton_yes.show()
        else:
            self.ui.pushButton_yes.hide()

        if showNo:
            self.ui.pushButton_no.show()
        else:
            self.ui.pushButton_no.hide()

    @pyqtSlot()
    def on_pushButton_no_clicked(self):
        self._selectedAnswer = self.NO
        self.close()

    @pyqtSlot()
    def on_pushButton_yes_clicked(self):
        self._selectedAnswer = self.YES
        self.close()

    @pyqtSlot()
    def on_pushButton_cancel_clicked(self):
        self._selectedAnswer = self.CANCEL
        self.close()

    @pyqtSlot()
    def on_pushButton_ok_clicked(self):
        self._selectedAnswer = self.OK
        self.close()

    def exec(self):
        super().exec()
        return self._selectedAnswer