# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainapp.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 694)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_central = QtWidgets.QStackedWidget(self.centralwidget)
        self.widget_central.setObjectName("widget_central")
        self.page_welcom = QtWidgets.QWidget()
        self.page_welcom.setObjectName("page_welcom")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_welcom)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.page_welcom)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.label_2 = QtWidgets.QLabel(self.page_welcom)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.widget_central.addWidget(self.page_welcom)
        self.page_test = QtWidgets.QWidget()
        self.page_test.setObjectName("page_test")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_test)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.layout_test = QtWidgets.QVBoxLayout()
        self.layout_test.setObjectName("layout_test")
        self.verticalLayout_4.addLayout(self.layout_test)
        self.widget_central.addWidget(self.page_test)
        self.page_mode = QtWidgets.QWidget()
        self.page_mode.setObjectName("page_mode")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_mode)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.layout_mode = QtWidgets.QVBoxLayout()
        self.layout_mode.setObjectName("layout_mode")
        self.verticalLayout_5.addLayout(self.layout_mode)
        self.widget_central.addWidget(self.page_mode)
        self.verticalLayout.addWidget(self.widget_central)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setObjectName("pushButton_start")
        self.horizontalLayout.addWidget(self.pushButton_start)
        self.pushButton_next = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_next.setObjectName("pushButton_next")
        self.horizontalLayout.addWidget(self.pushButton_next)
        self.pushButton_startMode = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_startMode.setObjectName("pushButton_startMode")
        self.horizontalLayout.addWidget(self.pushButton_startMode)
        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.horizontalLayout.addWidget(self.pushButton_exit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.widget_central.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Low cost ventilator"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/images/images/lung.png\"/></p></body></html>"))
        self.pushButton_start.setText(_translate("MainWindow", "Start"))
        self.pushButton_next.setText(_translate("MainWindow", "Next"))
        self.pushButton_startMode.setText(_translate("MainWindow", "Start Mode"))
        self.pushButton_exit.setText(_translate("MainWindow", "Exit"))


from .ressourceimages_rc import *

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

