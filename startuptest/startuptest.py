
from .testimplementation.abstractstartuptest import AbstractStartUpTest
from .startuptestwidget import StartUpTestWidget


class StartUpTest:

    def __init__(self):
        # Get all startup test to be applied
        allStartUpTestClassList = AbstractStartUpTest.getAllSubclasses()

        # Create an instance variable that is a dict containing each test instance and if it's succeed
        self.instanceList = list()
        for aStartUpClass in allStartUpTestClassList:
            instance = aStartUpClass()
            self.instanceList.append(instance)

    def getAllTestInstancesList(self):
        return self.instanceList

    def computeAllTest(self):
        for aTestInstance in self.instanceList:
            if aTestInstance is None:
                continue
            succeed, error = aTestInstance.computeTest()
            if not succeed:
                return False, error

        return True, ''

    def getAllTestAreValid(self):
        return all([instance.getTestSucceed() for instance in self.instanceList])

    def getAssociatedWidget(self, parent):
        return StartUpTestWidget(parent, self)
