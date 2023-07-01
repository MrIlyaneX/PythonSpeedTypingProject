from PyQt6 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_CreateAccount(object):
    def loginCheck(self):
        username = self.UsernameInput.text()
        password = self.PasswordInput.text()
        # initializing database
        # it is incorrect, should be redone for another db interface
        connection = sqlite3.connect("createAccount")
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
            from SameUsername import Ui_SameUsername
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_SameUsername()
            self.ui.setupUi(self.window)
            self.window.show()

    def Back(self):
        from MAIN_WINDOW import Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(231, 255, 239);\n"
                                 "")
        MainWindow.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Createaccount = QtWidgets.QLabel(parent=self.centralwidget)
        self.Createaccount.setGeometry(QtCore.QRect(0, 0, 801, 181))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Createaccount.sizePolicy().hasHeightForWidth())
        self.Createaccount.setSizePolicy(sizePolicy)
        self.Createaccount.setMinimumSize(QtCore.QSize(0, 181))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.Createaccount.setFont(font)
        self.Createaccount.setAcceptDrops(False)
        self.Createaccount.setToolTipDuration(-1)
        self.Createaccount.setStyleSheet(" background-color: rgb(194, 255, 172);\n"
                                         "")
        self.Createaccount.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.Createaccount.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.Createaccount.setScaledContents(False)
        self.Createaccount.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Createaccount.setWordWrap(False)
        self.Createaccount.setIndent(-1)
        self.Createaccount.setObjectName("Createaccount")
        self.Write_your_nameLbl = QtWidgets.QLabel(parent=self.centralwidget)
        self.Write_your_nameLbl.setGeometry(QtCore.QRect(290, 190, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.Write_your_nameLbl.setFont(font)
        self.Write_your_nameLbl.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                              "border-radius: 25px;")
        self.Write_your_nameLbl.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.Write_your_nameLbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Write_your_nameLbl.setObjectName("Write_your_nameLbl")
        self.Create_a_passwordLbl = QtWidgets.QLabel(parent=self.centralwidget)
        self.Create_a_passwordLbl.setGeometry(QtCore.QRect(290, 460, 201, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Create_a_passwordLbl.sizePolicy().hasHeightForWidth())
        self.Create_a_passwordLbl.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.Create_a_passwordLbl.setFont(font)
        self.Create_a_passwordLbl.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.Create_a_passwordLbl.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                                "border-radius: 25px;")
        self.Create_a_passwordLbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Create_a_passwordLbl.setObjectName("Create_a_passwordLbl")
        self.NameText = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.NameText.setGeometry(QtCore.QRect(300, 270, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.NameText.setFont(font)
        self.NameText.setStyleSheet("\n"
                                    "background-color: rgb(255, 255, 255);")
        self.NameText.setObjectName("NameText")
        self.PasswordText = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.PasswordText.setGeometry(QtCore.QRect(300, 540, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.PasswordText.setFont(font)
        self.PasswordText.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PasswordText.setObjectName("PasswordText")
        self.SaveBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.SaveBtn.setGeometry(QtCore.QRect(622, 517, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.SaveBtn.setFont(font)
        self.SaveBtn.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                   "border-radius: 25px;")
        self.SaveBtn.setObjectName("SaveBtn")
        self.BackBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.BackBtn.setGeometry(QtCore.QRect(50, 517, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.BackBtn.setFont(font)
        self.BackBtn.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                   "border-radius: 25px;\n"
                                   "")
        self.BackBtn.setObjectName("BackBtn")
        # Button action to come back to the MainWindow
        self.BackBtn.clicked.connect(self.Back)
        self.BackBtn.clicked.connect(MainWindow.close)
        self.emailText = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.emailText.setGeometry(QtCore.QRect(300, 400, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.emailText.setFont(font)
        self.emailText.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.emailText.setObjectName("emailText")
        self.Email_Lbl = QtWidgets.QLabel(parent=self.centralwidget)
        self.Email_Lbl.setGeometry(QtCore.QRect(290, 320, 201, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Email_Lbl.sizePolicy().hasHeightForWidth())
        self.Email_Lbl.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.Email_Lbl.setFont(font)
        self.Email_Lbl.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.Email_Lbl.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                     "border-radius: 25px;")
        self.Email_Lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Email_Lbl.setObjectName("Email_Lbl")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setToolTip(
            _translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.Createaccount.setText(_translate("MainWindow", "Create an account"))
        self.Write_your_nameLbl.setText(_translate("MainWindow", "Write you name"))
        self.Create_a_passwordLbl.setText(_translate("MainWindow", "Create a password"))
        self.SaveBtn.setText(_translate("MainWindow", "Save"))
        self.BackBtn.setText(_translate("MainWindow", "Back"))
        self.Email_Lbl.setText(_translate("MainWindow", "Write your e-mail"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_CreateAccount()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
