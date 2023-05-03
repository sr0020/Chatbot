import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import os
import sys

qtCreatorFile = os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])), "main_window.ui")
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
# print(form_secondwindow)

class secondwindow(QDialog, QWidget, Ui_MainWindow, QtBaseClass):
    def __init__(self):
        super(secondwindow.self).__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.home.clicked.connect(self.Home)

    def Home(self):
        self.close()