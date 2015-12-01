# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys
import steuerung


class UI(steuerung.Ui_Steurung):
    def __init__(self, w):
        self.window = w
        super().setupUi(self.window)


app = QtGui.QApplication(sys.argv)

w = QtGui.QWidget()
i = UI(w)
w.show()
sys.exit(app.exec_())

