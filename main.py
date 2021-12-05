import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QLineEdit
from PyQt5.QtGui import QPixmap

class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("main.ui",self)

app = QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(730)
widget.setWindowOpacity(1)
widget.setFixedWidth(1072)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
