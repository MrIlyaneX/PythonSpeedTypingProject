# Form implementation generated from reading ui file 'Account.ui'
#
# Created by: PyQt6 UI code generator 6.5.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Account(object):
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
        self.Info = QtWidgets.QPushButton(parent=self.frame)
        self.Info.setGeometry(QtCore.QRect(290, 40, 221, 81))
        self.Info.setStyleSheet("background-color: rgb(235, 255, 197);\n"
"border-radius: 25px;")
        self.Info.setObjectName("Info")
        self.Info_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Info_2.setGeometry(QtCore.QRect(40, 210, 331, 61))
        self.Info_2.setStyleSheet("background-color: rgb(235, 255, 197);\n"
"border-radius: 25px;")
        self.Info_2.setObjectName("Info_2")
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(60, 290, 301, 61))
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser.setObjectName("textBrowser")
        self.Info_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Info_3.setGeometry(QtCore.QRect(500, 300, 221, 61))
        self.Info_3.setStyleSheet("background-color: rgb(235, 255, 197);\n"
"border-radius: 25px;")
        self.Info_3.setObjectName("Info_3")
        self.Info_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Info_4.setGeometry(QtCore.QRect(40, 430, 271, 61))
        self.Info_4.setStyleSheet("background-color: rgb(235, 255, 197);\n"
"border-radius: 25px;")
        self.Info_4.setObjectName("Info_4")
        self.Info_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Info_5.setGeometry(QtCore.QRect(170, 500, 121, 61))
        self.Info_5.setStyleSheet("background-color: rgb(235, 255, 197);\n"
"border-radius: 25px;")
        self.Info_5.setObjectName("Info_5")
        self.textBrowser_2 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(80, 500, 81, 51))
        self.textBrowser_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(530, 370, 171, 61))
        self.textBrowser_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.back = QtWidgets.QPushButton(parent=self.centralwidget)
        self.back.setGeometry(QtCore.QRect(610, 520, 171, 61))
        self.back.setStyleSheet("background-color: rgb(235, 255, 197);\n"
"border-radius: 25px;")
        self.back.setObjectName("back")
        Account.setCentralWidget(self.centralwidget)

        self.retranslateUi(Account)
        QtCore.QMetaObject.connectSlotsByName(Account)

    def retranslateUi(self, Account):
        _translate = QtCore.QCoreApplication.translate
        Account.setWindowTitle(_translate("Account", "MainWindow"))
        self.Info.setText(_translate("Account", "Account"))
        self.Info_2.setText(_translate("Account", "Username"))
        self.Info_3.setText(_translate("Account", "Your Best Time"))
        self.Info_4.setText(_translate("Account", "You are with us already"))
        self.Info_5.setText(_translate("Account", "days"))
        self.back.setText(_translate("Account", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Account = QtWidgets.QMainWindow()
    ui = Ui_Account()
    ui.setupUi(Account)
    Account.show()
    sys.exit(app.exec())
