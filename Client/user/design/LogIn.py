import sqlite3
import sqlite3
from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_LogIn(object):
    def loginCheck(self):
        username = self.UsernameInput.text()
        password = self.PasswordInput.text()

        # initializing database
        # it is incorrect, should be redone for another db interface
        connection = sqlite3.connect("login")
        result = connection.execute("SELECT + FROM USERS WHERE USERNAME = ? AND PASSWORD = ?", (username, password))
        # checking if the user have found
        if len(result.fetchall()) > 0:
            # if the user was found we will close the window and go to the MainWindow
            from MAIN_WINDOW import Ui_MainWindow
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.window)
            self.window.show()
        else:  # if the user was not found we will force user to try one more time and show the error btn
            from IncorrectPassword import Ui_IncorrectPassword
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_IncorrectPassword()
            self.ui.setupUi(self.window)
            self.window.show()

    def Back(self):
        from MAIN_WINDOW import Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        # self.window.show()
    def setupUi(self, LogInWindow):
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
        # Button action to come back to the MainWindow
        self.logIn_button.clicked.connect(self.loginCheck)

        # self.logIn_button.clicked.connect(self.Back)
        # self.logIn_button.clicked.connect(LogInWindow.close)

        self.UsernameInput = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.UsernameInput.setGeometry(QtCore.QRect(310, 270, 181, 41))
        self.UsernameInput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.UsernameInput.setObjectName("UsernameInput")
        self.PasswordInput = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.PasswordInput.setGeometry(QtCore.QRect(310, 530, 181, 41))
        self.PasswordInput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PasswordInput.setObjectName("PasswordInput")
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
        self.backbtn.clicked.connect(self.Back)
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
        LogInWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LogInWindow)
        QtCore.QMetaObject.connectSlotsByName(LogInWindow)

    def retranslateUi(self, LogInWindow):
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
    ui.setupUi(LogInWindow)
    LogInWindow.show()
    sys.exit(app.exec())
