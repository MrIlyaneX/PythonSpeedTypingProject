from PyQt6 import QtCore, QtWidgets


class IncorrectPassword(object):
    def setup_ui(self):
        """
        Sets up the user interface for the main window.

        :param self: The instance of the class that this function belongs to.
        :return: None
        """
        self.central_widget = QtWidgets.QWidget()
        self.central_widget.setObjectName("same_username")
        self.central_widget.resize(396, 229)
        self.central_widget.setStyleSheet("background-color: rgb(194, 255, 172);\n"
                                          "font: 12pt \"Arial Rounded MT Bold\";\n"
                                          "")

        self.incorrect_lbl = QtWidgets.QLabel(parent=self.central_widget)
        self.incorrect_lbl.setGeometry(QtCore.QRect(20, 30, 361, 61))
        self.incorrect_lbl.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                         "border-radius: 25px;")
        self.incorrect_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.incorrect_lbl.setObjectName("IncorrectLbl")

        self.try_again_lbl = QtWidgets.QLabel(parent=self.central_widget)
        self.try_again_lbl.setGeometry(QtCore.QRect(90, 130, 231, 51))
        self.try_again_lbl.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                         "border-radius: 25px;")
        self.try_again_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.try_again_lbl.setObjectName("TryAgainLbl")

        self.retranslate_ui()
        QtCore.QMetaObject.connectSlotsByName(self.central_widget)

    def retranslate_ui(self):
        """
        This function sets the translated text for various UI elements in the main window.

        :return: None
        """
        _translate = QtCore.QCoreApplication.translate
        self.central_widget.setWindowTitle(_translate("IncorrectPassword", "Form"))
        self.incorrect_lbl.setText(_translate("IncorrectPassword", "Incorrect Username or Password"))
        self.try_again_lbl.setText(_translate("IncorrectPassword", "Please, try again"))
