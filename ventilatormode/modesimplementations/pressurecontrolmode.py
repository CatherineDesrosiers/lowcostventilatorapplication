
from ventilatormode.modesimplementations.ventilatormodeabstract import VentilatorModeAbstract


class PressureControlMode(VentilatorModeAbstract):

    def __init__(self):
        super().__init__()

    @classmethod
    def getAssociatedModeName(cls):
        """
        Return the mode name to be displayed
        :return: str
        """
        return 'Pressure Control Ventilation'

    def startMode(self):
        """
        Put here to code to be excuted for the current mode

        :return: bool, a callable function
        """
        return True, None
