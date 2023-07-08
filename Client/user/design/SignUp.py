from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QStackedWidget, QWidget

from Client import SharedData


class SignUpWindow(QWidget):
    def __init__(self, shared_data: SharedData):
        super().__init__()
        self.shared_data = shared_data

    def open_main(self):
        """
        Opens the Main window by setting the current index of the stacked widget to 1.

        :param self: The instance of the class that this method belongs to.
        :return: None
        """
        self.stacked_widget.setCurrentIndex(1)

    def open_login(self):
        """
        Opens the LogIn window by setting the current index of the stacked widget to 2.

        :param self: The instance of the class that this method belongs to.
        :return: None
        """
        self.stacked_widget.setCurrentIndex(2)

    def open_create_acc(self):
        """
        Opens the CreateAccount window by setting the current index of the stacked widget to 4.

        :param self: The instance of the class that this method belongs to.
        :return: None
        """
        self.stacked_widget.setCurrentIndex(4)

    def exit_program(self):
        """
        This function closes the program.

        :param self: The instance of the class that this method belongs to.
        :return: None
        """
        QtWidgets.QApplication.quit()

    def setup_ui(self, stacked_widget: QStackedWidget):
        """
        Sets up the user interface for the main window.

        :param self: The instance of the class that this function belongs to.
        :return: None
        """
        self.stacked_widget = stacked_widget

        self.central_widget = QtWidgets.QWidget(parent=stacked_widget)
        self.central_widget.setObjectName("central_widget")

        self.sign_up_widget = QtWidgets.QLabel(parent=self.central_widget)
        self.sign_up_widget.setGeometry(QtCore.QRect(0, -10, 801, 181))
        self.sign_up_widget.setFont(QtGui.QFont("Arial Rounded MT Bold", 16))
        self.sign_up_widget.setStyleSheet("background-color: rgb(194, 255, 172);\n"
                                          "border-radius: 10px;")
        self.sign_up_widget.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.sign_up_widget.setObjectName("sign_up_widget")

        self.sign_up_button = QtWidgets.QPushButton(parent=self.central_widget)
        self.sign_up_button.setGeometry(QtCore.QRect(260, 200, 291, 101))
        self.sign_up_button.setFont(QtGui.QFont("Arial Rounded MT Bold", 12))
        self.sign_up_button.setStyleSheet("""QPushButton:hover{background-color: rgb(235, 255, 197); 
                                                            border: 1px solid black;
                                                            border-radius: 25px;}
                                                         QPushButton:!hover{background-color: rgb(235, 255, 197);
                                                          border-radius: 25px;}
                                                            """)
        self.sign_up_button.setObjectName("sign_up_button")
        self.sign_up_button.clicked.connect(self.open_create_acc)

        self.login_button = QtWidgets.QPushButton(parent=self.central_widget)
        self.login_button.setGeometry(QtCore.QRect(260, 320, 291, 101))
        self.login_button.setFont(QtGui.QFont("Arial Rounded MT Bold", 12))
        self.login_button.setStyleSheet("""QPushButton:hover{background-color: rgb(235, 255, 197); 
                                                            border: 1px solid black;
                                                            border-radius: 25px;}
                                                         QPushButton:!hover{background-color: rgb(235, 255, 197);
                                                          border-radius: 25px;}
                                                            """)
        self.login_button.setObjectName("login_button")
        self.login_button.clicked.connect(self.open_login)

        self.without_account_button = QtWidgets.QPushButton(parent=self.central_widget)
        self.without_account_button.setGeometry(QtCore.QRect(260, 440, 291, 101))
        self.without_account_button.setFont(QtGui.QFont("Arial Rounded MT Bold", 12))
        self.without_account_button.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                                  "border-radius: 25px;")
        self.without_account_button.setObjectName("without_account_button")
        self.without_account_button.setStyleSheet("""QPushButton:hover{background-color: rgb(235, 255, 197); 
                                                    border: 1px solid black;
                                                    border-radius: 25px;}
                                                 QPushButton:!hover{background-color: rgb(235, 255, 197);
                                                  border-radius: 25px;}
                                                    """)
        self.without_account_button.clicked.connect(self.open_main)

        stacked_widget.addWidget(self.central_widget)
        self.retranslate_ui()

    def retranslate_ui(self):
        """
        This function sets the translated text for various UI elements in the main window.

        :return: None
        """
        _translate = QtCore.QCoreApplication.translate
        self.central_widget.setWindowTitle(_translate("SignUpWindow", "Sign Up"))
        self.sign_up_widget.setText(_translate("SignUpWindow", "Want to sign up?"))
        self.sign_up_button.setText(_translate("SignUpWindow", "Sign Up"))
        self.login_button.setText(_translate("SignUpWindow", "Log in"))
        self.without_account_button.setText(_translate("SignUpWindow", "Continue without an account"))
