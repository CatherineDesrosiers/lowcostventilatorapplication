
from messagedialog.custummessagedialog import CustumMessageDialog

from .modesimplementations.ventilatormodeabstract import VentilatorModeAbstract
from .ventilatorwidget import VentilatorWidget


class Ventilator:

    def __init__(self):
        self.availableModes = [None]
        VentilatorModeAbstract.getAllSubclasses(self.availableModes)

        self.selectedModeInstance = None

    def getWidget(self, parent=None):
        return VentilatorWidget(parent=parent, model=self)

    def getModeWidget(self, parent=None):
        if self.selectedModeInstance is None:
            return None

        return self.selectedModeInstance.getModeWidget(parent)

    def getAvailableVentilatorMode(self):
        return self.availableModes

    def setInspiratoryPressure(self, inspiratoryPressure):
        if self.selectedModeInstance is None:
            return

        self.selectedModeInstance.setInspiratoryPressure(inspiratoryPressure)

    def getInspiratoryPressure(self):
        if self.selectedModeInstance is None:
            return 0
        return self.selectedModeInstance.getInspiratoryPressure()

    def getExpiratoryPressure(self):
        if self.selectedModeInstance is None:
            return 0
        return self.selectedModeInstance.getExpiratoryPressure()

    def setExpiratoryPressure(self, expiratoryPressure):
        if self.selectedModeInstance is None:
            return

        self.selectedModeInstance.setExpiratoryPressure(expiratoryPressure)

    def getLowerValueForInspiratoryPressure(self):
        if self.selectedModeInstance is None:
            return 0
        return self.selectedModeInstance.getLowerValueForInspiratoryPressure()

    def getLowerValueForExpiratoryPressure(self):
        if self.selectedModeInstance is None:
            return 0
        return self.selectedModeInstance.getLowerValueForExpiratoryPressure()

    def getHigherValueForInspiratoryPressure(self):
        if self.selectedModeInstance is None:
            return 0
        return self.selectedModeInstance.getHigherValueForInspiratoryPressure()

    def getHigherValueForExpiratoryPressure(self):
        if self.selectedModeInstance is None:
            return 0
        return self.selectedModeInstance.getHigherValueForExpiratoryPressure()

    def getVolume(self):
        if self.selectedModeInstance is None:
            return 0

        return self.selectedModeInstance.getVolume()

    def setVolume(self, volume):
        if self.selectedModeInstance is None:
            return 0

        return self.selectedModeInstance.setVolume(volume)

    def getSelectedModeInstance(self):
        return self.selectedModeInstance

    def setSelectedModeClass(self, selectedModeClass):
        if selectedModeClass is None:
            self.selectedModeInstance = None
            return

        self.selectedModeInstance = selectedModeClass()

    def invalidSelectedMode(self, parent):
        # TODO FIX ME
        CustumMessageDialog(parent, )

    def getIsValidParameters(self):
        if self.selectedModeInstance is None:
            return False, 'Please select a ventilator mode'

        return self.selectedModeInstance.getIsValidParameters()

    def startMode(self):
        # valid params
        if self.selectedModeInstance is None:
            return False, self.invalidSelectedMode

        isValid, error = self.selectedModeInstance.getIsValidParameters()
        if not isValid:
            return False, self.selectedModeInstance.displayError

        succeed, functionToCall = self.selectedModeInstance.startMode()
        if not succeed:
            return False, functionToCall

        return True, None