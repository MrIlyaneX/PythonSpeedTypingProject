from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QStackedWidget


class Ui_IncorrectPassword(object):
    def open_main(self):
        self.stacked_widget.setCurrentIndex(0)

    def setup_ui(self, stacked_widget: QStackedWidget):
        self.stacked_widget = stacked_widget

        IncorrectPassword = QtWidgets.QWidget()
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

        self.retranslate_ui(IncorrectPassword)
        QtCore.QMetaObject.connectSlotsByName(IncorrectPassword)

        stacked_widget.addWidget(IncorrectPassword)

    def retranslate_ui(self, IncorrectPassword):
        _translate = QtCore.QCoreApplication.translate
        IncorrectPassword.setWindowTitle(_translate("IncorrectPassword", "Form"))
        self.IncorrectLbl.setText(_translate("IncorrectPassword", "Incorrect Username or Password"))
        self.TryAgainLbl.setText(_translate("IncorrectPassword", "Please, try again"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    stacked_widget = QStackedWidget()
    stacked_widget.setFixedSize(396, 229)

    incorrect_password_window = Ui_IncorrectPassword()
    incorrect_password_window.setup_ui(stacked_widget)

    main_window = QtWidgets.QMainWindow()
    main_window.setCentralWidget(stacked_widget)
    main_window.show()

    sys.exit(app.exec())
