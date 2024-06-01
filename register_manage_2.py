import sys
from PySide6 import QtCore, QtGui, QtWidgets
from check_db import *
from auth_window2 import *


class Registration(QtWidgets.QMainWindow):
    def __init__(self):
        super(Registration, self).__init__()
        self.ui = Auth_Window2()
        self.ui.setupUi(self)
        self.ui.RegButt.clicked.connect()
        self.ui.LoginButt.clicked.connect(self.login)


if __name__ == "__main__":
    App = QtWidgets.QApplication([])
    window_reg = Registration()
    window_reg.show()
    sys.exit(App.exec())
