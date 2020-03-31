from ventilatormode.modesimplementations.ventilatormodeabstract import VentilatorModeAbstract

from .ui.assistcontrolwidget import AssistControlWidget


class AssistControlMode(VentilatorModeAbstract):

    def __init__(self):
        super().__init__()
        self.rate = 6
        self.lowerRateValue = 5
        self.higherRateValue = 40

    @classmethod
    def getAssociatedModeName(cls):
        """
        Return the mode name to be displayed
        :return: str
        """
        return 'Assistance Control (CMV)'

    def getRate(self):
        return self.rate

    def setRate(self, rate):
        self.rate = rate

    def getLowerValueForRate(self):
        return self.lowerRateValue

    def getHigherValueForRate(self):
        return self.higherRateValue

    def getModeWidget(self, parent):
        return AssistControlWidget(parent=parent, model=self)

    def _getIsValidParameters(self):
        """
        Return true if all instances parameters are valid. False otherwise
        :return: bool
        """

        if not self.lowerRateValue <= self.rate <= self.higherRateValue:
            return False, f'Selected rate value must be between {self.lowerRateValue} breaths a minute' \
                          f'and {self.higherRateValue} breaths a minute.'

        return True, ''


