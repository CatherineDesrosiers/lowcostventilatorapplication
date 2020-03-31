from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot

from messagedialog.custummessagedialog import CustumMessageDialog
from startuptest.startuptest import StartUpTest
from ventilatormode.ventilator import Ventilator

from .ui_mainapp import Ui_MainWindow


class MainAppWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        # TODO A model should be done, view got to much knowlage for now
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Init Starting page
        self.ui.pushButton_next.hide()
        self.ui.pushButton_startMode.hide()
        self.ui.widget_central.setCurrentIndex(0)
        self.ui.widget_central.complete = False

        # Instance and widget page 1 (maintenance and calibration)
        self.startUpTestInstance = None
        self.startUpTestWidget = None

        # Instance and widget page 2 (mode setup)
        self.modeInstance = None
        self.modeWidget = None

    def nextPage(self):
        current_page = self.ui.widget_central.currentIndex()
        i = int(current_page) + 1
        self.ui.widget_central.setCurrentIndex(i)

# ------------------------------- EXIT -------------------------------
    @pyqtSlot()
    def on_pushButton_exit_clicked(self):
        dialog = CustumMessageDialog(parent=self, message='Are you sure you want to exit the program ? If so the '
                                                          'system will shutdown.',
                                     windowTitle='Exit', showYes=True, showCancel=True)
        answer = dialog.exec()
        if answer == CustumMessageDialog.CANCEL:
            return

        if self.modeInstance is not None:
            pass  # TODO: call function to stop all component

        self.close()

# ------------------------------- Init page 1-------------------------------
    @pyqtSlot()
    def on_pushButton_start_clicked(self):
        # Increment to next page, which is start up component test.
        self.nextPage()
        self.ui.pushButton_start.hide()

        dialog = CustumMessageDialog(parent=self,
                                     message='Calibration and maintenance will now be computed. This might take a '
                                             'while...',
                                     windowTitle='Calibration and maintenance', showOk=True)
        dialog.exec()
        self.startUpTestInstance = StartUpTest()

        succeed, fctToCall = self.startUpTestInstance.computeAllTest()

        self.startUpTestWidget = self.startUpTestInstance.getAssociatedWidget(self)
        self.ui.layout_test.addWidget(self.startUpTestWidget)
        self.startUpTestWidget.updateUI()
        self.ui.pushButton_next.show()
        if not succeed and callable(fctToCall):
            self.ui.pushButton_next.setEnabled()
            fctToCall(self)

    # ------------------------------- Init page 2 -------------------------------
    @pyqtSlot()
    def on_pushButton_next_clicked(self):
        self.nextPage()
        self.ui.pushButton_next.hide()

        # RE
        self.startUpTestInstance = None
        self.startUpTestWidget = None

        dialog = CustumMessageDialog(parent=self,
                                     message='Select the wished ventilator mode and set input parameters',
                                     windowTitle='Ventilator Mode', showOk=True)
        dialog.exec()

        self.modeInstance = Ventilator()
        self.modeWidget = self.modeInstance.getWidget(self)
        self.ui.layout_mode.addWidget(self.modeWidget)
        self.ui.pushButton_startMode.show()

    # ------------------- Validate selected param and init page 3 -------------------------------
    @pyqtSlot()
    def on_pushButton_startMode_clicked(self):
        if self.modeInstance is None:
            return

        isAllParamValid, errorToDisplay = self.modeInstance.getIsValidParameters()
        if not isAllParamValid:
            d = CustumMessageDialog(self, errorToDisplay, 'Start mode error', showOk=True)
            d.exec()
            return

        # If all input are good , start application
        d = CustumMessageDialog(self, 'Application will now start', showOk=True)
        d.exec()

        succeed, functionToBeCalled = self.modeInstance.startMode()
        if not succeed and callable(functionToBeCalled):
            try:
                functionToBeCalled(self)
            except Exception as e:
                pass