
from ..messagedialog.custummessagedialog import CustumMessageDialog
from .alarm import Alarm


class ErrorAndAlarmsHelper:

    @staticmethod
    def highPressureAlarm(parent):
        ErrorAndAlarmsHelper.renderErrorAndManageAlarm(parent, 'Pressure is too high', 'High Pressure Error')

    @staticmethod
    def lowPressureAlarm(parent):
        ErrorAndAlarmsHelper.renderErrorAndManageAlarm(parent, 'Pressure is too low', 'Low Pressure Error')

    @staticmethod
    def respiratorySystemIssue(parent):
        ErrorAndAlarmsHelper.renderErrorAndManageAlarm(parent, 'Current respiratory cycle is not normal',
                                                       'Respiratory Cycle Error')

    @staticmethod
    def renderErrorAndManageAlarm(parent, errorMessage, windowTitle):
        errrorMessage = CustumMessageDialog(parent, f'{errorMessage}. The program will now exit',
                                            windowTitle, showOk=True)
        Alarm.startAlarm()
        errrorMessage.exec()
        Alarm.stopAlarm()
