from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SameUsername(object):
    def setupUi(self, SameUsername):
        SameUsername.setObjectName("SameUsername")
        SameUsername.resize(396, 229)
        SameUsername.setStyleSheet(" background-color: rgb(194, 255, 172);\n"
"font: 12pt \"Arial Rounded MT Bold\";\n"
"")
        self.ErrorLbl = QtWidgets.QLabel(parent=SameUsername)
        self.ErrorLbl.setGeometry(QtCore.QRect(40, 40, 321, 61))
        self.ErrorLbl.setStyleSheet("background-color: rgb(235, 255, 197);\n"
"border-radius: 25px;")
        self.ErrorLbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ErrorLbl.setObjectName("ErrorLbl")
        self.NewUsernameLbl = QtWidgets.QLabel(parent=SameUsername)
        self.NewUsernameLbl.setGeometry(QtCore.QRect(10, 140, 371, 61))
        self.NewUsernameLbl.setStyleSheet("background-color: rgb(235, 255, 197);\n"
"border-radius: 25px;")
        self.NewUsernameLbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.NewUsernameLbl.setObjectName("NewUsernameLbl")

        self.retranslateUi(SameUsername)
        QtCore.QMetaObject.connectSlotsByName(SameUsername)

    def retranslateUi(self, SameUsername):
        _translate = QtCore.QCoreApplication.translate
        SameUsername.setWindowTitle(_translate("SameUsername", "Form"))
        self.ErrorLbl.setText(_translate("SameUsername", "This Username already exists"))
        self.NewUsernameLbl.setText(_translate("SameUsername", "Please, insert new Username"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SameUsername = QtWidgets.QWidget()
    ui = Ui_SameUsername()
    ui.setupUi(SameUsername)
    SameUsername.show()
    sys.exit(app.exec())
