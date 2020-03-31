from startuptest.testimplementation.abstractstartuptest import AbstractStartUpTest


class Pressure2StartUpTest(AbstractStartUpTest):

    @classmethod
    def getTestName(cls):
        """
        Return the test name that will be display

        :return: str
        """
        return 'Pressure 2'

    def computeTest(self):
        """
        Here should be defined the code to be called

        :return: True if the test succeed, False otherwise
        :rtype: bool
        :return: string the give information about the error
        :rtype: str
        """

        # TODO !
        # Do not focget to set self.succeed = True at the end
        self.succeed = True
        return True, ''
