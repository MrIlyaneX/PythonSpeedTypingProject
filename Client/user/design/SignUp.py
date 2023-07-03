from PyQt6 import QtCore, QtGui, QtWidgets
from MAIN_WINDOW import Ui_MainWindow
from LogIn import Ui_LogIn
from CreateAccount import Ui_CreateAccount

from PyQt6.QtWidgets import QStackedWidget


# comments

class Ui_SignUp(object):
    def open_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setup_ui(self.window)
        SignUpWindow.hide()
        self.window.show()

    def create_acc(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_CreateAccount()
        self.ui.setup_ui(self.window)
        SignUpWindow.hide()
        self.window.show()

    def open_log_in(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_LogIn()
        self.ui.setup_ui(self.window)
        SignUpWindow.hide()
        self.window.show()

    def setup_ui(self, SignUpWindow):
        SignUpWindow.setObjectName("SignUpWindow")
        SignUpWindow.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        SignUpWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setKerning(True)
        SignUpWindow.setFont(font)
        SignUpWindow.setStyleSheet("background-color: rgb(231, 255, 239);")
        SignUpWindow.setAnimated(True)
        SignUpWindow.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.centralwidget = QtWidgets.QWidget(parent=SignUpWindow)
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
        self.SignUpBtn.setGeometry(QtCore.QRect(260, 200, 291, 101))
        self.SignUpBtn.clicked.connect(self.create_acc)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        font.setKerning(False)
        self.SignUpBtn.setFont(font)
        self.SignUpBtn.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                     "border-radius: 25px;\n"
                                     "")
        self.SignUpBtn.setCheckable(True)
        self.SignUpBtn.setFlat(False)
        self.SignUpBtn.setObjectName("SignUpBtn")
        self.LogInBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.LogInBtn.setGeometry(QtCore.QRect(260, 320, 291, 101))
        font = QtGui.QFont()
        self.LogInBtn.clicked.connect(self.open_log_in)
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.LogInBtn.setFont(font)
        self.LogInBtn.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                    "border-radius: 25px;\n"
                                    "")
        self.LogInBtn.setObjectName("LogInBtn")
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
        self.WithoutAccBtn.clicked.connect(self.open_window)
        SignUpWindow.setCentralWidget(self.centralwidget)

        self.retranslate_ui(SignUpWindow)
        self.SignUpBtn.clicked.connect(self.centralwidget.hide)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(SignUpWindow)

    def retranslate_ui(self, SignUpWindow):
        _translate = QtCore.QCoreApplication.translate
        SignUpWindow.setWindowTitle(_translate("SignUpWindow", "Sign Up"))
        self.SignUpMenu.setText(_translate("SignUpWindow", "Want to sign up?"))
        self.SignUpBtn.setText(_translate("SignUpWindow", "Sign Up"))
        self.LogInBtn.setText(_translate("SignUpWindow", "Log in"))
        self.WithoutAccBtn.setText(_translate("SignUpWindow", "Continue without an account"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    SignUpWindow = QtWidgets.QMainWindow()
    ui = Ui_SignUp()
    ui.setup_ui(SignUpWindow)
    SignUpWindow.show()
    sys.exit(app.exec())
