

class AbstractStartUpTest:

    def __init__(self):
        self.succeed = False

    def getTestSucceed(self):
        return self.succeed

    @classmethod
    def getTestName(cls):
        """
        Return the test name that will be display

        :return: str
        """
        raise NotImplementedError('getTestName should be implemented')

    def computeTest(self):
        """
        Here should be defined the code to be called

        :return: True if the test succeed, False otherwise
        :rtype: bool
        :return: string the give information about the error
        :rtype: str
        """
        return True, ''

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
