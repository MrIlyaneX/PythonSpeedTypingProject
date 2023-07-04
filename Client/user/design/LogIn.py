from PyQt6 import QtCore, QtGui, QtWidgets
from Client.client_runner import *
from PyQt6.QtWidgets import QStackedWidget, QWidget, QMainWindow


class LogInWindow(QWidget):

    def open_main(self):
        self.stacked_widget.setCurrentIndex(0)

    def open_signup(self):
        self.stacked_widget.setCurrentIndex(3)

    def get_username(self):
        return self.UsernameInput.text()

    def get_password(self):
        return self.PasswordInput.text()

    def get_email(self):
        return self.EmailTxt.text()

    def log_in(self):
        username = self.get_username()
        password = self.get_password()
        user_email = self.get_email()
        print(user_email, username, password)
        header = get_header(username=username, password=password, user_email=user_email, to_login=True)
        print(header)
        return header

    def setup_ui(self, stacked_widget: QStackedWidget):
        self.stacked_widget = stacked_widget

        self.setObjectName("self")
        self.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.setFont(font)
        self.setStyleSheet("background-color: rgb(231, 255, 239);")
        self.central_widget = QtWidgets.QWidget(self)
        self.central_widget.setObjectName("centralwidget")
        self.LogIn = QtWidgets.QLabel(self.central_widget)
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

        self.Username = QtWidgets.QLabel(self.central_widget)
        self.Username.setGeometry(QtCore.QRect(300, 180, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.Username.setFont(font)
        self.Username.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                    "border-radius: 25px;")
        self.Username.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Username.setObjectName("Username")

        self.Password = QtWidgets.QLabel(self.central_widget)
        self.Password.setGeometry(QtCore.QRect(300, 450, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.Password.setFont(font)
        self.Password.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                    "border-radius: 25px;")
        self.Password.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Password.setObjectName("Password")

        self.logIn_button = QtWidgets.QPushButton(self.central_widget)
        self.logIn_button.setGeometry(QtCore.QRect(622, 517, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.logIn_button.setFont(font)
        self.logIn_button.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                        "border-radius: 25px;\n"
                                        "")
        self.logIn_button.setObjectName("logIn_button")

        self.UsernameInput = QtWidgets.QLineEdit(self.central_widget)
        self.UsernameInput.setGeometry(QtCore.QRect(310, 270, 181, 41))
        self.UsernameInput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.UsernameInput.setObjectName("UsernameInput")

        self.PasswordInput = QtWidgets.QLineEdit(self.central_widget)
        self.PasswordInput.setGeometry(QtCore.QRect(310, 530, 181, 41))
        self.PasswordInput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PasswordInput.setObjectName("PasswordInput")

        self.backbtn = QtWidgets.QPushButton(self.central_widget)
        self.backbtn.setGeometry(QtCore.QRect(50, 517, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.backbtn.setFont(font)
        self.backbtn.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                   "border-radius: 25px;\n"
                                   "")
        self.backbtn.setObjectName("backbtn")

        self.EmailLbl = QtWidgets.QLabel(self.central_widget)
        self.EmailLbl.setGeometry(QtCore.QRect(300, 320, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.EmailLbl.setFont(font)
        self.EmailLbl.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                    "border-radius: 25px;")
        self.EmailLbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.EmailLbl.setObjectName("EmailLbl")

        self.EmailTxt = QtWidgets.QLineEdit(self.central_widget)
        self.EmailTxt.setGeometry(QtCore.QRect(310, 400, 181, 41))
        self.EmailTxt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.EmailTxt.setObjectName("EmailTxt")

        self.logIn_button.clicked.connect(self.log_in)

        # was back
        self.backbtn.clicked.connect(self.open_main)

        stacked_widget.addWidget(self.central_widget)
        self.retranslate_ui()

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "MainWindow"))
        self.LogIn.setText(_translate("self", "Log in"))
        self.Username.setText(_translate("self", "Username"))
        self.Password.setText(_translate("self", "Password"))
        self.logIn_button.setText(_translate("self", "Log in"))
        self.backbtn.setText(_translate("self", "Back"))
        self.EmailLbl.setText(_translate("self", "E-mail"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    stacked_widget = QStackedWidget()
    stacked_widget.setFixedSize(800, 600)
    stacked_widget.show()

    login_window = LogInWindow(stacked_widget)
    stacked_widget.addWidget(login_window)

    sys.exit(app.exec())
