# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventilatorwidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 457)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox_selectedMode = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_selectedMode.sizePolicy().hasHeightForWidth())
        self.comboBox_selectedMode.setSizePolicy(sizePolicy)
        self.comboBox_selectedMode.setObjectName("comboBox_selectedMode")
        self.horizontalLayout.addWidget(self.comboBox_selectedMode)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_volume = QtWidgets.QLineEdit(Form)
        self.lineEdit_volume.setObjectName("lineEdit_volume")
        self.horizontalLayout_2.addWidget(self.lineEdit_volume)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_inspiratoryPressure = QtWidgets.QHBoxLayout()
        self.horizontalLayout_inspiratoryPressure.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_inspiratoryPressure.setObjectName("horizontalLayout_inspiratoryPressure")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_inspiratoryPressure.addWidget(self.label_3)
        self.horizontalSlider_inspiratoryPressure = QtWidgets.QSlider(Form)
        self.horizontalSlider_inspiratoryPressure.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_inspiratoryPressure.setObjectName("horizontalSlider_inspiratoryPressure")
        self.horizontalLayout_inspiratoryPressure.addWidget(self.horizontalSlider_inspiratoryPressure)
        self.lineEdit_inspiratoryPressure = QtWidgets.QLineEdit(Form)
        self.lineEdit_inspiratoryPressure.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineEdit_inspiratoryPressure.setObjectName("lineEdit_inspiratoryPressure")
        self.horizontalLayout_inspiratoryPressure.addWidget(self.lineEdit_inspiratoryPressure)
        self.verticalLayout.addLayout(self.horizontalLayout_inspiratoryPressure)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.horizontalSlider_expiratoryPressure = QtWidgets.QSlider(Form)
        self.horizontalSlider_expiratoryPressure.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_expiratoryPressure.setObjectName("horizontalSlider_expiratoryPressure")
        self.horizontalLayout_4.addWidget(self.horizontalSlider_expiratoryPressure)
        self.lineEdit_expiratoryPressure_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_expiratoryPressure_2.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineEdit_expiratoryPressure_2.setObjectName("lineEdit_expiratoryPressure_2")
        self.horizontalLayout_4.addWidget(self.lineEdit_expiratoryPressure_2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.layout_selectedVentilatorMode = QtWidgets.QVBoxLayout()
        self.layout_selectedVentilatorMode.setContentsMargins(-1, -1, -1, 0)
        self.layout_selectedVentilatorMode.setObjectName("layout_selectedVentilatorMode")
        self.verticalLayout.addLayout(self.layout_selectedVentilatorMode)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Select ventilator mode"))
        self.label_2.setText(_translate("Form", "Volume (mm):"))
        self.label_3.setText(_translate("Form", "Inspiratory pressure (cmH20)"))
        self.label_5.setText(_translate("Form", "Expiratory pressure (cmH20) "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

