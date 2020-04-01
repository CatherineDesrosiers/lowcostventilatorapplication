# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'messagedialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MessageDialog(object):
    def setupUi(self, MessageDialog):
        MessageDialog.setObjectName("MessageDialog")
        MessageDialog.resize(444, 139)
        self.verticalLayout = QtWidgets.QVBoxLayout(MessageDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_message = QtWidgets.QLabel(MessageDialog)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_message.setFont(font)
        self.label_message.setText("")
        self.label_message.setObjectName("label_message")
        self.verticalLayout.addWidget(self.label_message)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_ok = QtWidgets.QPushButton(MessageDialog)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_ok.setFont(font)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.horizontalLayout.addWidget(self.pushButton_ok)
        self.pushButton_yes = QtWidgets.QPushButton(MessageDialog)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_yes.setFont(font)
        self.pushButton_yes.setObjectName("pushButton_yes")
        self.horizontalLayout.addWidget(self.pushButton_yes)
        self.pushButton_no = QtWidgets.QPushButton(MessageDialog)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_no.setFont(font)
        self.pushButton_no.setObjectName("pushButton_no")
        self.horizontalLayout.addWidget(self.pushButton_no)
        self.pushButton_cancel = QtWidgets.QPushButton(MessageDialog)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_cancel.setFont(font)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout.addWidget(self.pushButton_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(MessageDialog)
        QtCore.QMetaObject.connectSlotsByName(MessageDialog)

    def retranslateUi(self, MessageDialog):
        _translate = QtCore.QCoreApplication.translate
        MessageDialog.setWindowTitle(_translate("MessageDialog", "Dialog"))
        self.pushButton_ok.setText(_translate("MessageDialog", "OK"))
        self.pushButton_yes.setText(_translate("MessageDialog", "Yes"))
        self.pushButton_no.setText(_translate("MessageDialog", "No"))
        self.pushButton_cancel.setText(_translate("MessageDialog", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MessageDialog = QtWidgets.QDialog()
    ui = Ui_MessageDialog()
    ui.setupUi(MessageDialog)
    MessageDialog.show()
    sys.exit(app.exec_())

