# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WigetMessageboxGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(391, 171)
        Form.setStyleSheet("")
        self.CloseBtn = QtWidgets.QPushButton(Form)
        self.CloseBtn.setGeometry(QtCore.QRect(133, 130, 121, 31))
        self.CloseBtn.setObjectName("CloseBtn")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(15, 10, 361, 20))
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(15, 30, 361, 91))
        self.textBrowser.setObjectName("textBrowser")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 391, 171))
        self.label_2.setStyleSheet("border: 2px solid rgb(39, 68, 255);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.CloseBtn.raise_()
        self.label.raise_()
        self.textBrowser.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.CloseBtn.setText(_translate("Form", "OK"))
        self.label.setText(_translate("Form", "Title"))
