from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QMainWindow


class IncorrectPassword(QMainWindow):
    """
    This class is responsible for the warning window.
    """
    def setup_ui(self):
        """
        Sets up the user interface for the main window.

        :param self: The instance of the class that this function belongs to.
        :return: None
        """

        self.setObjectName("same_username")
        self.setFixedSize(396, 229)
        self.setStyleSheet("background-color: rgb(194, 255, 172);\n"
                           "font: 12pt \"Arial Rounded MT Bold\";\n"
                           "")

        central_widget = QtWidgets.QWidget(self)
        central_widget.setObjectName("central_widget")

        incorrect_lbl = QtWidgets.QLabel(parent=central_widget)
        incorrect_lbl.setGeometry(QtCore.QRect(20, 30, 361, 61))
        incorrect_lbl.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                    "border-radius: 25px;")
        incorrect_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        incorrect_lbl.setObjectName("IncorrectLbl")

        try_again_lbl = QtWidgets.QLabel(parent=central_widget)
        try_again_lbl.setGeometry(QtCore.QRect(90, 130, 231, 51))
        try_again_lbl.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                    "border-radius: 25px;")
        try_again_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        try_again_lbl.setObjectName("TryAgainLbl")

        self.setCentralWidget(central_widget)

        self.retranslate_ui()

    def retranslate_ui(self):
        """
        This function sets the translated text for various UI elements in the main window.

        :return: None
        """
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("IncorrectPassword", "Form"))
        self.centralWidget().findChild(QtWidgets.QLabel, "IncorrectLbl").setText(
            _translate("IncorrectPassword", "Incorrect Username or Password"))
        self.centralWidget().findChild(QtWidgets.QLabel, "TryAgainLbl").setText(
            _translate("IncorrectPassword", "Please, try again"))
