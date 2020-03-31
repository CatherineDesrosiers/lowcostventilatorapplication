from messagedialog.custummessagedialog import CustumMessageDialog


class VentilatorModeAbstract:
    """
    Abstract class for ventilator modes

    TODO these functions should be implemented in subclasses
    -  getAssociatedModeName()
    - _getIsValidParameters()
    - startMode()

    ..Note: See the section: Method to be implemented/ overloaded if needed
    """

    def __init__(self):
        self.volume = 0
        self.form = None
        self.lastError = ''

        self.pressureInspiratory = 0
        self.lowerLimitPressureInspiratory = 0
        self.higherLimitPressureInspiratory = 40

        self.pressureExpiratory = 0
        self.lowerLimitPressureExpiratory = 0
        self.higherLimitPressureExpiratory = 20

    def setInspiratoryPressure(self, inspiratoryPressure):
        self.pressureInspiratory = inspiratoryPressure

    def getInspiratoryPressure(self, ):
        return self.pressureInspiratory

    def getExpiratoryPressure(self):
        return self.pressureExpiratory

    def setExpiratoryPressure(self, expiratoryPressure):
        self.pressureExpiratory = expiratoryPressure

    def getLowerValueForInspiratoryPressure(self):
        return self.lowerLimitPressureInspiratory

    def getLowerValueForExpiratoryPressure(self):
        return self.lowerLimitPressureExpiratory

    def getHigherValueForInspiratoryPressure(self):
        return self.higherLimitPressureInspiratory

    def getHigherValueForExpiratoryPressure(self):
        return self.higherLimitPressureExpiratory

    def getPressureUnitStr(self):
        return 'cmH20'

    def getVolume(self):
        return self.volume

    def setVolume(self, volume):
        self.volume = volume

    def getVolumeUnitStr(self):
        return 'mm'

    def displayError(self, parent):
        d = CustumMessageDialog(parent, self.lastError, f'{self.getAssociatedModeName()}', showOk=True)
        d.exec()

    def getIsValidParameters(self):
        """
        Return true if all instances parameters are valid. False otherwise.
        Should give more information for cases that a parameter is not valid.

        :return: bool, error
        """
        isVolumValid = self.volume > 0
        if not isVolumValid:
            return isVolumValid, 'Invalid input volume'

        if not self.lowerLimitPressureInspiratory <= self.pressureInspiratory <= self.higherLimitPressureInspiratory:
            return False, f'Selected inspiratory value must be between {self.lowerLimitPressureInspiratory} cmH20 ' \
                          f'and {self.higherLimitPressureInspiratory} cmH2O.'

        if not self.lowerLimitPressureExpiratory <= self.pressureExpiratory <= self.higherLimitPressureExpiratory:
            return False, f'Selected expiratory value must be between {self.lowerLimitPressureExpiratory} cmH20 ' \
                          f'and {self.higherLimitPressureExpiratory} cmH2O.'

        return self._getIsValidParameters()

# --------------------------------- Method to be implemented/ overloaded if needed----------------------------------
    @classmethod
    def getAssociatedModeName(cls):
        """
        Return the mode name to be displayed
        :return: str
        """
        raise NotImplementedError('getAssociatedModeName() should be implemented')

    def _getIsValidParameters(self):
        """
        Return true if all instances parameters are valid. False otherwise.
        Should give more information for cases that a parameter is not valid.

        :return: bool, error
        """
        return True, ''

    def prepareToDelete(self):
        """
        Free memory here or remove python ref on instance variable
        """
        pass

    def startMode(self):
        """
        Put here to code to be executed for the current mode

        :return: bool, a callable function to be call if an error occur
        """
        raise NotImplementedError('startMode() should be implemented')

    def exitMode(self):
        """
        """
        pass

    def getWidget(self, parent):
        return None

    def getModeWidget(self, parent):
        return None

# ------------------------------------ Abstract Class stuff ------------------------------------
    @classmethod
    def getAllSubclasses(cls, subclassesList=None):
        """
        getAllSubsetClasses
        :param subclassesList: a list of subclasses
        :type subclassesList: list

        :return: a filled list of subclasses
        :rtype: list
        """
        if subclassesList is None:
            subclassesList = list()

        mySubclasses = cls.__subclasses__()
        for aSubclass in mySubclasses:
            subclassesList.append(aSubclass)
            aSubclass.getAllSubclasses(subclassesList)

        return subclassesList
