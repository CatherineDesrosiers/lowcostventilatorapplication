import weakref
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSlot

from .ui_assistantcontrolmode import Ui_Form


class AssistControlWidget(QWidget):

    def __init__(self, parent=None, model=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self._model = weakref.ref(model) if model is not None else None

        self.ui.lineEdit_rate.blockSignals(True)
        self.ui.lineEdit_rate.setEnabled(False)
        self.ui.lineEdit_rate.blockSignals(False)


    def getModel(self):
        return self._model()

    def closeEvent(self, event):
        model = self.getModel()
        if model is not None:
            model.prepareToDelete()

        super().closeEvent(event)

    def updateUI(self):
        if self.getModel() is None:
            return

        rate = self.getModel().getRate()
        minValue = self.getModel().getLowerValueForRate()
        maxValue = self.getModel().getHigherValueForRate()

        self.ui.lineEdit_rate.blockSignals(True)
        self.ui.horizontalSlider_rate.blockSignals(True)
        self.ui.lineEdit_rate.setText(str(rate))
        self.ui.horizontalSlider_rate.setRange(minValue, maxValue)
        self.ui.horizontalSlider_rate.setValue(rate)
        self.ui.horizontalSlider_rate.singleStep()
        self.ui.lineEdit_rate.blockSignals(False)
        self.ui.horizontalSlider_rate.blockSignals(False)

    @pyqtSlot()
    def on_horizontalSlider_rate_sliderReleased(self):
        if self.getModel() is None:
            return None

        value = self.ui.horizontalSlider_rate.value()
        self.getModel().setRate(value)
        self.updateUI()