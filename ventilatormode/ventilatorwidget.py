import weakref
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget
from .ui_ventilatorwidget import Ui_Form


class VentilatorWidget(QWidget):

    def __init__(self, parent=None, model=None):
        super().__init__(parent=parent)

        # init ui
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Instance variables
        self.parent = parent
        self._model = weakref.ref(model) if model is not None else None
        self._widgetMode = None

        self.ui.lineEdit_inspiratoryPressure.blockSignals(True)
        self.ui.lineEdit_inspiratoryPressure.setEnabled(False)
        self.ui.lineEdit_inspiratoryPressure.blockSignals(False)

        self.ui.lineEdit_expiratoryPressure_2.blockSignals(True)
        self.ui.lineEdit_expiratoryPressure_2.setEnabled(False)
        self.ui.lineEdit_expiratoryPressure_2.blockSignals(False)

        self.updateUI()

    def updateUI(self):
        if self.getModel() is None:
            return

        # Init combobox
        self.ui.comboBox_selectedMode.blockSignals(True)
        self.ui.comboBox_selectedMode.clear()
        availableModeClass = self.getModel().getAvailableVentilatorMode()
        for aClass in availableModeClass:
            classNameToDisplay = aClass.getAssociatedModeName() if aClass is not None else 'Choose a ventilator mode'
            self.ui.comboBox_selectedMode.addItem(classNameToDisplay, aClass)

        selectedInstance = self.getModel().getSelectedModeInstance()
        selectedInstanceName = selectedInstance.getAssociatedModeName() if selectedInstance is not None else \
            'Choose a ventilator mode'
        self.ui.comboBox_selectedMode.setCurrentText(selectedInstanceName)
        self.ui.comboBox_selectedMode.blockSignals(False)

        # Update ui volume
        selectedVolume = self.getModel().getVolume()
        self.ui.lineEdit_volume.blockSignals(True)
        self.ui.lineEdit_volume.setText(str(selectedVolume))
        self.ui.lineEdit_volume.blockSignals(False)

        # Enabled UI
        self._enableForSelectedInstance()

        if self._widgetMode is not None:
            self._widgetMode.close()
            self.ui.layout_selectedVentilatorMode.removeWidget(self._widgetMode)
            self._widgetMode = None

        # Remove reference on widget if selected instance is None
        if selectedInstance is None:
            self._widgetMode = None
            return

        # Update pressure values
        pressureValueInsp = self.getModel().getInspiratoryPressure()
        lowerValueInsp = self.getModel().getLowerValueForInspiratoryPressure()
        higherValueInsp = self.getModel().getHigherValueForInspiratoryPressure()
        self.ui.horizontalSlider_inspiratoryPressure.blockSignals(True)
        self.ui.lineEdit_inspiratoryPressure.blockSignals(True)
        self.ui.lineEdit_inspiratoryPressure.setText(str(pressureValueInsp))
        self.ui.horizontalSlider_inspiratoryPressure.setRange(lowerValueInsp, higherValueInsp)
        self.ui.horizontalSlider_inspiratoryPressure.singleStep()
        self.ui.horizontalSlider_inspiratoryPressure.setValue(pressureValueInsp)
        self.ui.horizontalSlider_inspiratoryPressure.blockSignals(False)
        self.ui.lineEdit_inspiratoryPressure.blockSignals(False)

        pressureValueExp = self.getModel().getExpiratoryPressure()
        lowerValueExp = self.getModel().getLowerValueForExpiratoryPressure()
        higherValueExp = self.getModel().getHigherValueForExpiratoryPressure()
        self.ui.horizontalSlider_expiratoryPressure.blockSignals(True)
        self.ui.lineEdit_expiratoryPressure_2.blockSignals(True)
        self.ui.lineEdit_expiratoryPressure_2.setText(str(pressureValueExp))
        self.ui.horizontalSlider_expiratoryPressure.setRange(lowerValueExp, higherValueExp)
        self.ui.horizontalSlider_expiratoryPressure.setValue(pressureValueExp)
        self.ui.horizontalSlider_expiratoryPressure.blockSignals(False)
        self.ui.lineEdit_expiratoryPressure_2.blockSignals(False)

        # Init widget Instance
        if self._widgetMode is None:
            selectedModeWidget = self.getModel().getModeWidget(self)
            if selectedModeWidget is None:
                self._widgetMode = None
                return
            self._widgetMode = selectedModeWidget 

        # Update selected mode widget  UI
        self._widgetMode.updateUI()
        self.ui.layout_selectedVentilatorMode.addWidget(self._widgetMode)

    def _enableForSelectedInstance(self):
        if self.getModel() is None:
            return

        enabled = self.getModel().getSelectedModeInstance() is not None

        # Volume
        self.ui.lineEdit_volume.blockSignals(True)
        self.ui.lineEdit_volume.setEnabled(enabled)
        self.ui.lineEdit_volume.blockSignals(False)

        # Inspiratory stuff
        self.ui.horizontalSlider_expiratoryPressure.blockSignals(True)
        self.ui.horizontalSlider_expiratoryPressure.setEnabled(enabled)
        self.ui.horizontalSlider_expiratoryPressure.blockSignals(False)

        self.ui.horizontalSlider_inspiratoryPressure.blockSignals(True)
        self.ui.horizontalSlider_inspiratoryPressure.setEnabled(enabled)
        self.ui.horizontalSlider_inspiratoryPressure.blockSignals(False)

    def getModel(self):
        return self._model()

    def closeEvent(self, event):
        model = self.getModel()
        if model is not None:
            model.prepareToDelete()

        super().closeEvent(event)

    @pyqtSlot()
    def on_pushButton_start_clicked(self):
        model = self.getModel()
        if model is None:
            return

        model.confirmSelectedParameter()

        isStarted, fct = model.startMode()

        if not isStarted and callable(fct):
            fct(self)

    @pyqtSlot()
    def on_lineEdit_volume_editingFinished(self):
        if self.getModel() is None:
            return
        newValueStr = self.ui.lineEdit_volume.text()
        newValue = float(newValueStr)
        self.getModel().setVolume(newValue)
        self.updateUI()

    @pyqtSlot(str)
    def on_comboBox_selectedMode_currentTextChanged(self, selectedModeStr):
        if self.getModel() is None:
            return

        selectedModeClass = self.ui.comboBox_selectedMode.currentData()
        self.getModel().setSelectedModeClass(selectedModeClass)
        self.updateUI()

    @pyqtSlot()
    def on_horizontalSlider_expiratoryPressure_sliderReleased(self):
        if self.getModel() is None:
            return None

        value = self.ui.horizontalSlider_expiratoryPressure.value()
        self.getModel().setExpiratoryPressure(value)
        self.updateUI()

    @pyqtSlot()
    def on_horizontalSlider_inspiratoryPressure_sliderReleased(self):
        if self.getModel() is None:
            return None

        value = self.ui.horizontalSlider_inspiratoryPressure.value()
        self.getModel().setInspiratoryPressure(value)
        self.updateUI()
