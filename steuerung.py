# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './steurung.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_Steurung(object):
    def setupUi(self, Steurung):
        Steurung.setObjectName(_fromUtf8("Steurung"))
        Steurung.resize(214, 416)
        self.gridLayout = QtGui.QGridLayout(Steurung)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox_2 = QtGui.QGroupBox(Steurung)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.comboBox = QtGui.QComboBox(self.groupBox_2)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.gridLayout_4.addWidget(self.comboBox, 0, 0, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout_4.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 2, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(Steurung)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_2.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout_2.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(Steurung)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout_3.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.horizontalSlider = QtGui.QSlider(self.groupBox_3)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.gridLayout_3.addWidget(self.horizontalSlider, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_3, 1, 0, 1, 1)

        self.retranslateUi(Steurung)
        QtCore.QMetaObject.connectSlotsByName(Steurung)

    def retranslateUi(self, Steurung):
        Steurung.setWindowTitle(_translate("Steurung", "Steuerung", None))
        self.groupBox_2.setTitle(_translate("Steurung", "GroupBox", None))
        self.pushButton_3.setText(_translate("Steurung", "PushButton", None))
        self.groupBox.setTitle(_translate("Steurung", "GroupBox", None))
        self.pushButton.setText(_translate("Steurung", "Start", None))
        self.pushButton_2.setText(_translate("Steurung", "Stop", None))
        self.groupBox_3.setTitle(_translate("Steurung", "GroupBox", None))

