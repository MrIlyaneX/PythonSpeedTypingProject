from PyQt6 import QtCore, QtGui, QtWidgets
class Ui_Account(object):
    def Back(self):
        from MAIN_WINDOW import Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        # self.window.show()

    def setupUi(self, Account):
        Account.setObjectName("Account")
        Account.resize(800, 600)
        Account.setStyleSheet("background-color: rgb(231, 255, 239);\n"
"font: 12pt \"Arial Rounded MT Bold\";")
        self.centralwidget = QtWidgets.QWidget(parent=Account)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 181))
        self.frame.setStyleSheet(" background-color: rgb(194, 255, 172);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.AccountLbl = QtWidgets.QLabel(parent=self.frame)
        self.AccountLbl.setGeometry(QtCore.QRect(300, 50, 221, 81))
        self.AccountLbl.setStyleSheet("background-color: rgb(235, 255, 197);\n"
"border-radius: 25px;")
        self.AccountLbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.AccountLbl.setObjectName("AccountLbl")
        self.UsernameTxt = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.UsernameTxt.setGeometry(QtCore.QRect(60, 290, 301, 61))
        self.UsernameTxt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.UsernameTxt.setObjectName("UsernameTxt")
        self.DaysTxt = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.DaysTxt.setGeometry(QtCore.QRect(80, 500, 81, 51))
        self.DaysTxt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.DaysTxt.setObjectName("DaysTxt")
        self.TimeTxt = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.TimeTxt.setGeometry(QtCore.QRect(530, 370, 171, 61))
        self.TimeTxt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.TimeTxt.setObjectName("TimeTxt")
        self.backBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.backBtn.setGeometry(QtCore.QRect(630, 530, 151, 51))
        self.backBtn.setStyleSheet("background-color: rgb(235, 255, 197);\n"
"border-radius: 25px;")
        self.backBtn.setObjectName("backBtn")
        # Button action to come back to the MainWindow
        self.backBtn.clicked.connect(self.Back)
        self.backBtn.setAutoDefault(False)
        self.backBtn.clicked.connect(Account.close)
        self.backBtn.setAutoDefault(False)

        # from MAIN_WINDOW123 import Ui_MainWindow
        # self.sub_window = Ui_MainWindow()
        # self.backBtn.clicked.connect(self.sub_window.show)

        self.UsernameLbl = QtWidgets.QLabel(parent=self.centralwidget)
        self.UsernameLbl.setGeometry(QtCore.QRect(40, 220, 331, 61))
        self.UsernameLbl.setStyleSheet("background-color: rgb(235, 255, 197);\n"
"border-radius: 25px;")
        self.UsernameLbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.UsernameLbl.setObjectName("UsernameLbl")
        self.TimeLbl = QtWidgets.QLabel(parent=self.centralwidget)
        self.TimeLbl.setGeometry(QtCore.QRect(500, 300, 221, 61))
        self.TimeLbl.setStyleSheet("background-color: rgb(235, 255, 197);\n"
"border-radius: 25px;")
        self.TimeLbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.TimeLbl.setObjectName("TimeLbl")
        self.DaysLbl = QtWidgets.QLabel(parent=self.centralwidget)
        self.DaysLbl.setGeometry(QtCore.QRect(170, 500, 121, 61))
        self.DaysLbl.setStyleSheet("background-color: rgb(235, 255, 197);\n"
"border-radius: 25px;")
        self.DaysLbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.DaysLbl.setObjectName("DaysLbl")
        self.WithUsLbl = QtWidgets.QLabel(parent=self.centralwidget)
        self.WithUsLbl.setGeometry(QtCore.QRect(40, 430, 271, 61))
        self.WithUsLbl.setStyleSheet("background-color: rgb(235, 255, 197);\n"
"border-radius: 25px;")
        self.WithUsLbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.WithUsLbl.setObjectName("WithUsLbl")
        Account.setCentralWidget(self.centralwidget)

        self.retranslateUi(Account)
        QtCore.QMetaObject.connectSlotsByName(Account)

    def retranslateUi(self, Account):
        _translate = QtCore.QCoreApplication.translate
        Account.setWindowTitle(_translate("Account", "MainWindow"))
        self.AccountLbl.setText(_translate("Account", "Account"))
        self.backBtn.setText(_translate("Account", "Back"))
        self.UsernameLbl.setText(_translate("Account", "Username"))
        self.TimeLbl.setText(_translate("Account", "Your best time"))
        self.DaysLbl.setText(_translate("Account", "days"))
        self.WithUsLbl.setText(_translate("Account", "You are with us already"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Account = QtWidgets.QMainWindow()
    ui = Ui_Account()
    ui.setupUi(Account)
    Account.show()
    sys.exit(app.exec())
