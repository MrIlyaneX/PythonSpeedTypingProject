from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QMainWindow


class SameUsernameWindow(QMainWindow):
    def setup_ui(self):
        """
        Sets up the user interface for the main window.

        :param self: The instance of the class that this function belongs to.
        :return: None
        """
        self.setObjectName("same_username")
        self.resize(396, 229)
        self.setStyleSheet("background-color: rgb(194, 255, 172);\n"
                           "font: 12pt \"Arial Rounded MT Bold\";\n")

        central_widget = QtWidgets.QWidget(self)
        central_widget.setObjectName("central_widget")

        error_lbl = QtWidgets.QLabel(parent=central_widget)
        error_lbl.setGeometry(QtCore.QRect(40, 40, 321, 61))
        error_lbl.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                "border-radius: 25px;")
        error_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        error_lbl.setObjectName("error_lbl")

        new_username_lbl = QtWidgets.QLabel(parent=central_widget)
        new_username_lbl.setGeometry(QtCore.QRect(10, 140, 371, 61))
        new_username_lbl.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                       "border-radius: 25px;")
        new_username_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        new_username_lbl.setObjectName("new_username_lbl")

        self.setCentralWidget(central_widget)

        self.retranslate_ui()


def retranslate_ui(self):
    """
    This function sets the translated text for various UI elements in the main window.

    :return: None
    """
    _translate = QtCore.QCoreApplication.translate
    self.setWindowTitle(_translate("same_username", "Form"))
    self.centralWidget().findChild(QtWidgets.QLabel, "error_lbl").setText(
        _translate("same_username", "This Username already exists"))
    self.centralWidget().findChild(QtWidgets.QLabel, "new_username_lbl").setText(
        _translate("same_username", "Please, insert new Username"))
