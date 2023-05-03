import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import os

# form_class = uic.loadUiType("main_window.ui")[0]

qtCreatorFile = os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])), "main_window.ui")  # Type your file path
# print(os.path.abspath(os.path.dirname(sys.argv[0])))
# print(os.path.abspath)
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
print(Ui_MainWindow, QtBaseClass)

class MyWindow(QMainWindow, Ui_MainWindow, QtBaseClass):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()