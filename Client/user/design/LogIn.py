from PyQt6 import QtCore, QtGui, QtWidgets
from client_runner import *


class Ui_LogIn(object):
    # function for getting text from user (username)
    def get_username(self):
        text = self.UsernameInput.text()
        return text

    # function for getting text from user (password)
    def get_password(self):
        text = self.UsernameInput.text()
        return text

    # function for getting text from user (email)
    def get_email(self):
        text = self.UsernameInput.text()
        return text

    # function for closing this window
    def back(self):
        from MAIN_WINDOW import Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setup_ui(self.window)

    def setup_ui(self, LogInWindow):
        LogInWindow.setObjectName("LogInWindow")
        LogInWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(12)
        LogInWindow.setFont(font)
        LogInWindow.setStyleSheet("background-color: rgb(231, 255, 239);")
        self.centralwidget = QtWidgets.QWidget(parent=LogInWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.LogIn = QtWidgets.QLabel(parent=self.centralwidget)
        self.LogIn.setGeometry(QtCore.QRect(0, -10, 800, 181))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.LogIn.setFont(font)
        self.LogIn.setStyleSheet("background-color: rgb(194, 255, 172);")
        self.LogIn.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.LogIn.setObjectName("LogIn")

        self.Username = QtWidgets.QLabel(parent=self.centralwidget)
        self.Username.setGeometry(QtCore.QRect(300, 180, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.Username.setFont(font)
        self.Username.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                    "border-radius: 25px;")
        self.Username.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Username.setObjectName("Username")
        # self.Username.clicked.connect(self.getUsername)
        self.Password = QtWidgets.QLabel(parent=self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(300, 450, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.Password.setFont(font)
        self.Password.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                    "border-radius: 25px;")
        self.Password.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Password.setObjectName("Password")
        self.logIn_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.logIn_button.setGeometry(QtCore.QRect(622, 517, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.logIn_button.setFont(font)
        self.logIn_button.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                        "border-radius: 25px;\n"
                                        "")
        self.logIn_button.setObjectName("logIn_button")

        self.UsernameInput = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.UsernameInput.setGeometry(QtCore.QRect(310, 270, 181, 41))
        self.UsernameInput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.UsernameInput.setObjectName("UsernameInput")
        self.PasswordInput = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.PasswordInput.setGeometry(QtCore.QRect(310, 530, 181, 41))
        self.PasswordInput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PasswordInput.setObjectName("PasswordInput")
        # self.PasswordInput.clicked.connect(self.getPassword)
        self.backbtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.backbtn.setGeometry(QtCore.QRect(50, 517, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.backbtn.setFont(font)
        self.backbtn.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                   "border-radius: 25px;\n"
                                   "")
        self.backbtn.setObjectName("backbtn")

        # Button action to come back to the MainWindow
        self.backbtn.clicked.connect(self.back)
        self.backbtn.clicked.connect(LogInWindow.close)

        self.EmailLbl = QtWidgets.QLabel(parent=self.centralwidget)
        self.EmailLbl.setGeometry(QtCore.QRect(300, 320, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.EmailLbl.setFont(font)
        self.EmailLbl.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                    "border-radius: 25px;")
        self.EmailLbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.EmailLbl.setObjectName("EmailLbl")
        self.EmailTxt = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.EmailTxt.setGeometry(QtCore.QRect(310, 400, 181, 41))
        self.EmailTxt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.EmailTxt.setObjectName("EmailTxt")
        # self.EmailTxt.clicked.connect(self.getEmail)
        LogInWindow.setCentralWidget(self.centralwidget)

        self.retranslate_ui(LogInWindow)
        QtCore.QMetaObject.connectSlotsByName(LogInWindow)

        # function call from the external file to work with another db
        if self.logIn_button.clicked:
            get_header(self.logIn_button.clicked.connect(self.get_username),
                       self.logIn_button.clicked.connect(self.get_password),
                       self.logIn_button.clicked.connect(self.get_email), to_login=True)

        # Button also will erase everything from the user input if he will leave this window
        self.logIn_button.clicked.connect(self.PasswordInput.clear)
        self.logIn_button.clicked.connect(self.UsernameInput.clear)
        self.logIn_button.clicked.connect(self.EmailTxt.clear)

        self.logIn_button.clicked.connect(self.back)
        self.logIn_button.clicked.connect(LogInWindow.close)

    def retranslate_ui(self, LogInWindow):
        _translate = QtCore.QCoreApplication.translate
        LogInWindow.setWindowTitle(_translate("LogInWindow", "MainWindow"))
        self.LogIn.setText(_translate("LogInWindow", "Log in"))
        self.Username.setText(_translate("LogInWindow", "Username"))
        self.Password.setText(_translate("LogInWindow", "Password"))
        self.logIn_button.setText(_translate("LogInWindow", "Log in"))
        self.backbtn.setText(_translate("LogInWindow", "Back"))
        self.EmailLbl.setText(_translate("LogInWindow", "E-mail"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    LogInWindow = QtWidgets.QMainWindow()
    ui = Ui_LogIn()
    ui.setup_ui(LogInWindow)
    LogInWindow.show()
    sys.exit(app.exec())
