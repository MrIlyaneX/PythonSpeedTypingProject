from PyQt6 import QtCore, QtWidgets


class SameUsernameWindow(object):
    def setup_ui(self):
        self.central_widget = QtWidgets.QWidget()
        self.central_widget.setObjectName("same_username")
        self.central_widget.resize(396, 229)
        self.central_widget.setStyleSheet("background-color: rgb(194, 255, 172);\n"
                                          "font: 12pt \"Arial Rounded MT Bold\";\n"
                                          "")

        self.error_lbl = QtWidgets.QLabel(parent=self.central_widget)
        self.error_lbl.setGeometry(QtCore.QRect(40, 40, 321, 61))
        self.error_lbl.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                     "border-radius: 25px;")
        self.error_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.error_lbl.setObjectName("error_lbl")

        self.new_username_lbl = QtWidgets.QLabel(parent=self.central_widget)
        self.new_username_lbl.setGeometry(QtCore.QRect(10, 140, 371, 61))
        self.new_username_lbl.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                            "border-radius: 25px;")
        self.new_username_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.new_username_lbl.setObjectName("new_username_lbl")

        self.retranslate_ui()
        QtCore.QMetaObject.connectSlotsByName(self.central_widget)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.central_widget.setWindowTitle(_translate("same_username", "Form"))
        self.error_lbl.setText(_translate("same_username", "This Username already exists"))
        self.new_username_lbl.setText(_translate("same_username", "Please, insert new Username"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    ui = SameUsernameWindow()
    ui.setup_ui()
    ui.central_widget.show()

    sys.exit(app.exec())
