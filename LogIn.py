# Form implementation generated from reading ui file 'LogIn.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(231, 255, 239);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
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
        self.Username.setGeometry(QtCore.QRect(300, 200, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.Username.setFont(font)
        self.Username.setStyleSheet("background-color: rgb(235, 255, 197);\n"
"border-radius: 25px;")
        self.Username.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Username.setObjectName("Username")
        self.Password = QtWidgets.QLabel(parent=self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(300, 370, 201, 71))
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
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(310, 290, 181, 41))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(310, 460, 181, 41))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.LogIn.setText(_translate("MainWindow", "Log in"))
        self.Username.setText(_translate("MainWindow", "Username"))
        self.Password.setText(_translate("MainWindow", "Password"))
        self.logIn_button.setText(_translate("MainWindow", "Log in"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
