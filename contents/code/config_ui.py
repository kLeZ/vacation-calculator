# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/config.ui'
#
# Created by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_config(object):
    def setupUi(self, config):
        config.setObjectName(_fromUtf8("config"))
        config.resize(390, 80)
        self.sbTotalVacationDays = QtGui.QSpinBox(config)
        self.sbTotalVacationDays.setGeometry(QtCore.QRect(290, 10, 91, 22))
        self.sbTotalVacationDays.setObjectName(_fromUtf8("sbTotalVacationDays"))
        self.lblTotalVacationDays = QtGui.QLabel(config)
        self.lblTotalVacationDays.setGeometry(QtCore.QRect(10, 10, 121, 16))
        self.lblTotalVacationDays.setObjectName(_fromUtf8("lblTotalVacationDays"))
        self.txtCalPath = QtGui.QPlainTextEdit(config)
        self.txtCalPath.setGeometry(QtCore.QRect(10, 40, 271, 31))
        self.txtCalPath.setObjectName(_fromUtf8("txtCalPath"))
        self.pushButton = QtGui.QPushButton(config)
        self.pushButton.setGeometry(QtCore.QRect(290, 40, 90, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(config)
        QtCore.QMetaObject.connectSlotsByName(config)

    def retranslateUi(self, config):
        config.setWindowTitle(_translate("config", "Configuration of plasmoid", None))
        self.lblTotalVacationDays.setText(_translate("config", "Total Vacation Days: ", None))
        self.pushButton.setText(_translate("config", "Browse...", None))

