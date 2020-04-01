# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assistantcontrolmode.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 24)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_rate = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_rate.setFont(font)
        self.label_rate.setObjectName("label_rate")
        self.horizontalLayout.addWidget(self.label_rate)
        self.horizontalSlider_rate = QtWidgets.QSlider(Form)
        self.horizontalSlider_rate.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_rate.setObjectName("horizontalSlider_rate")
        self.horizontalLayout.addWidget(self.horizontalSlider_rate)
        self.lineEdit_rate = QtWidgets.QLineEdit(Form)
        self.lineEdit_rate.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEdit_rate.setFont(font)
        self.lineEdit_rate.setObjectName("lineEdit_rate")
        self.horizontalLayout.addWidget(self.lineEdit_rate)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_rate.setText(_translate("Form", "Rate (breaths a minute) "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

