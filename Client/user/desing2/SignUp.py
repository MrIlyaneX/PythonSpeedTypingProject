# Form implementation generated from reading ui file 'SignUp.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
from PyQt6 import QtCore, QtGui, QtWidgets
from MAIN_WINDOW import Ui_MainWindow1
from LogIn import Ui_LogInWindow
from creation_an_account import Ui_CreateAccW

class Ui_MainWindow2(object):

    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow1()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()

    def createAcc(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_CreateAccWindow()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()

    def openLogIn(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_LogInWindow()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()

    def setupUi(self, MainWindow2):
        MainWindow2.setObjectName("MainWindow2")
        MainWindow2.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        MainWindow2.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setKerning(True)
        MainWindow2.setFont(font)
        MainWindow2.setStyleSheet("background-color: rgb(231, 255, 239);")
        MainWindow2.setAnimated(True)
        MainWindow2.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow2)
        self.centralwidget.setObjectName("centralwidget")
        self.SignUpMenu = QtWidgets.QLabel(parent=self.centralwidget)
        self.SignUpMenu.setGeometry(QtCore.QRect(0, -10, 801, 181))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.SignUpMenu.setFont(font)
        self.SignUpMenu.setStyleSheet("background-color: rgb(194, 255, 172);\n"
"border-radius: 10px;")
        self.SignUpMenu.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.SignUpMenu.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.SignUpMenu.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.SignUpMenu.setScaledContents(False)
        self.SignUpMenu.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.SignUpMenu.setWordWrap(False)
        self.SignUpMenu.setIndent(-1)
        self.SignUpMenu.setOpenExternalLinks(False)
        self.SignUpMenu.setObjectName("SignUpMenu")
        self.SignUpBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.SignUpBtn.setGeometry(QtCore.QRect(280, 200, 241, 101))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        font.setKerning(False)
        self.SignUpBtn.setFont(font)
        self.SignUpBtn.setStyleSheet("background-color: rgb(235, 255, 197);\n"
"border-radius: 25px;\n"
"")
        self.SignUpBtn.setObjectName("SignUpBtn")

        self.SignUpBtn.clicked.connect(self.createAcc)

        self.LogInBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.LogInBtn.setGeometry(QtCore.QRect(280, 320, 241, 101))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.LogInBtn.setFont(font)
        self.LogInBtn.setStyleSheet("background-color: rgb(235, 255, 197);\n"
"border-radius: 25px;\n"
"")
        self.LogInBtn.setObjectName("LogInBtn")
        self.LogInBtn.clicked.connect(self.openLogIn)
        self.WithoutAccBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.WithoutAccBtn.setEnabled(True)
        self.WithoutAccBtn.setGeometry(QtCore.QRect(260, 440, 291, 101))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.WithoutAccBtn.sizePolicy().hasHeightForWidth())
        self.WithoutAccBtn.setSizePolicy(sizePolicy)
        self.WithoutAccBtn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(False)
        self.WithoutAccBtn.setFont(font)
        self.WithoutAccBtn.setMouseTracking(False)
        self.WithoutAccBtn.setTabletTracking(False)
        self.WithoutAccBtn.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.WithoutAccBtn.setAcceptDrops(False)
        self.WithoutAccBtn.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.WithoutAccBtn.setAutoFillBackground(False)
        self.WithoutAccBtn.setStyleSheet("background-color: rgb(235, 255, 197);\n"
"border-radius: 25px;\n"
"")
        self.WithoutAccBtn.setShortcut("")
        self.WithoutAccBtn.setAutoRepeat(False)
        self.WithoutAccBtn.setAutoExclusive(False)
        self.WithoutAccBtn.setObjectName("WithoutAccBtn")
        MainWindow2.setCentralWidget(self.centralwidget)

        self.WithoutAccBtn.clicked.connect(self.openWindow)

        self.retranslateUi(MainWindow2)
        self.WithoutAccBtn.clicked.connect(MainWindow2.hide)
        QtCore.QMetaObject.connectSlotsByName(MainWindow2)

    def retranslateUi(self, MainWindow2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow2.setWindowTitle(_translate("MainWindow2", "Sign Up"))
        self.SignUpMenu.setText(_translate("MainWindow2", "Want to sign up?"))
        self.SignUpBtn.setText(_translate("MainWindow2", "Sign Up"))
        self.LogInBtn.setText(_translate("MainWindow2", "Log in"))
        self.WithoutAccBtn.setText(_translate("MainWindow2", "Continue without an account"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
