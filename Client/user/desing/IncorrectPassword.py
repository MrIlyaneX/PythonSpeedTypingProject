from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_IncorrectPassword(object):
    def setupUi(self, IncorrectPassword):
        IncorrectPassword.setObjectName("IncorrectPassword")
        IncorrectPassword.resize(396, 229)
        IncorrectPassword.setStyleSheet(" background-color: rgb(194, 255, 172);\n"
"font: 12pt \"Arial Rounded MT Bold\";")
        self.IncorrectLbl = QtWidgets.QLabel(parent=IncorrectPassword)
        self.IncorrectLbl.setGeometry(QtCore.QRect(20, 30, 361, 61))
        self.IncorrectLbl.setStyleSheet("background-color: rgb(235, 255, 197);\n"
"border-radius: 25px;")
        self.IncorrectLbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.IncorrectLbl.setObjectName("IncorrectLbl")
        self.TryAgainLbl = QtWidgets.QLabel(parent=IncorrectPassword)
        self.TryAgainLbl.setGeometry(QtCore.QRect(90, 130, 231, 51))
        self.TryAgainLbl.setStyleSheet("background-color: rgb(235, 255, 197);\n"
"border-radius: 25px;")
        self.TryAgainLbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.TryAgainLbl.setObjectName("TryAgainLbl")

        self.retranslateUi(IncorrectPassword)
        QtCore.QMetaObject.connectSlotsByName(IncorrectPassword)

    def retranslateUi(self, IncorrectPassword):
        _translate = QtCore.QCoreApplication.translate
        IncorrectPassword.setWindowTitle(_translate("IncorrectPassword", "Form"))
        self.IncorrectLbl.setText(_translate("IncorrectPassword", "Incorrect Username or Password"))
        self.TryAgainLbl.setText(_translate("IncorrectPassword", "Please, try again"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    IncorrectPassword = QtWidgets.QWidget()
    ui = Ui_IncorrectPassword()
    ui.setupUi(IncorrectPassword)
    IncorrectPassword.show()
    sys.exit(app.exec())
