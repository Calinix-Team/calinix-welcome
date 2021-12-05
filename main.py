import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QLineEdit
from PyQt5.QtGui import QPixmap
import webbrowser

import subprocess as sb

def run(command):
    sb.run(command, shell=True)

class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("main.ui",self)
        self.reddit.clicked.connect(lambda: self.OpenW('https://reddit.com/r/CalinixOS'))
        self.tele.clicked.connect(lambda: self.OpenW('https://t.me/joinchat/_Sk3DB_FEbdhYTU1'))
        self.yt.clicked.connect(lambda: self.OpenW('https://www.youtube.com/channel/UCyyXcHm8UswsF0cjOX6fMng'))
        self.sourceforge.clicked.connect(lambda: self.OpenW('http://calinixos.sf.net'))
        self.gh.clicked.connect(lambda: self.OpenW('https://github.com/Calinix-Team/'))
        self.forum.clicked.connect(lambda: self.OpenW('https://calinixos.forummotion.com'))
        self.disc.clicked.connect(lambda: self.OpenW('https://tinyurl.com/calinixdisc'))
        self.wiki.clicked.connect(lambda: self.OpenW('https://calinixos.blogspot.com'))
        self.blog.clicked.connect(lambda: self.OpenW('https://calinixos.blogspot.com'))
        self.getinv.clicked.connect(lambda: self.OpenW('https://calinix-team.github.io'))
        self.install.clicked.connect(self.StartInstall)
        self.close.clicked.connect(self.Quit)
        self.setup.clicked.connect(self.StartInstall)
    
    def Quit(self):
        sys.exit(app._exec)
    
    def OpenW(self, url):
        webbrowser.open(url)

    def StartInstall(self):
        run("pkexec --disable-internal-agent \"/usr/bin/calamares\" \"$@\"")



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
