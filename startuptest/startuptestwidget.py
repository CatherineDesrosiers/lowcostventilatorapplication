import weakref
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QSpacerItem, QSizePolicy, QLabel

from .ui_startupwidget import Ui_Form
from .imageswidget.failwidget import FailWidget
from .imageswidget.succeedwidget import SucceedWidget


class StartUpTestWidget(QWidget):

    def __init__(self, parent=None, model=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self._model = weakref.ref(model) if model is not None else None
        self._layoutItemList = []

    def close(self):
        self._layoutItemList.clear()  # Remove python reference

    def getModel(self):
        return self._model()

    def updateUI(self):
        model = self.getModel()
        if model is None:
            return

        testInstanceList = self.getModel().getAllTestInstancesList()

        for aTest in testInstanceList:
            if aTest is None:
                continue

            currentTestLayout = QHBoxLayout()
            spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
            labelTest = QLabel(parent=self)
            labelTest.setText(aTest.getTestName())

            font = labelTest.font()
            font.setPointSize(14)
            labelTest.setFont(font)

            succeed = aTest.getTestSucceed()
            image = SucceedWidget(self) if succeed else FailWidget(self)
            image.resize(16, 16)

            labelStatus = QLabel(parent=self)
            status = 'Succeed' if aTest.getTestSucceed() else 'Fail'
            labelStatus.setText(status)
            font = labelStatus.font()
            font.setPointSize(14)
            labelStatus.setFont(font)

            currentTestLayout.addWidget(labelTest)
            currentTestLayout.addItem(spacer)
            currentTestLayout.addWidget(labelStatus)

            self.ui.layout_test.addItem(currentTestLayout)
            self._layoutItemList.append(currentTestLayout)
