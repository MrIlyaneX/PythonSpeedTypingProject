from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QStackedWidget, QWidget

<<<<<<< HEAD
from Client import SharedData
=======
>>>>>>> feature-setup-wizard
from Client.client_runner import *


class LogInWindow(QWidget):
    def __init__(self, shared_data: SharedData):
        super().__init__()
        self.shared_data = shared_data

    def open_main(self):
        """
        Opens the initial window by setting the current index of the stacked widget to 0.

        :param self: The instance of the class that this method belongs to.
        :return: None
        """
        self.stacked_widget.setCurrentIndex(0)

    def open_signup(self):
        """
        Opens the SignUp window by setting the current index of the stacked widget to 0.

        :param self: The instance of the class that this method belongs to.
        :return: None
        """
        self.stacked_widget.setCurrentIndex(3)

    def get_username(self):
        """
        Retrieves the username entered by the user.
        This function retrieves the text entered the username_input QLineEdit widget, which is
        assumed to be a username provided by the user.

        :param self: The instance of the class that this method belongs to.
        :return: The username entered by the user as a string.
        """
        return self.username_input.text()

    def get_password(self):
        """
        Retrieves the password entered by the user.
        This function retrieves the text entered the password_input QLineEdit widget, which is
        assumed to be a username provided by the user.

        :param self: The instance of the class that this method belongs to.
        :return: The password entered by the user as a string.
        """
        return self.password_input.text()

    def get_email(self):
        """
        Retrieves the email entered by the user.
        This function retrieves the text entered the email_txt QLineEdit widget, which is
        assumed to be a username provided by the user.

        :param self: The instance of the class that this method belongs to.
        :return: The password entered by the user as a string.
        """
        return self.email_txt.text()

    def log_in(self):
        """
        Enters the user's account using the collected information when the 'log in' button is clicked.

        This function retrieves the username, password, and user email by calling the get_username,
        get_password, and get_email functions, respectively. It then tries to get the header using
        the collected information by calling the get_header function with the appropriate arguments.
        If the header is successfully obtained, the current index of the stacked_widget is set to 1,
        which corresponds to a successful login page. The header is returned.

        If an exception occurs during the process, such as the user providing wrong information or
        already being registered, the 'error' window will be shown.

        :param self: The instance of the class that this method belongs to.
        :return: The header obtained from the get_header function if the login is successful.
        """
        username = self.get_username()
        password = self.get_password()
        user_email = self.get_email()
        try:
<<<<<<< HEAD
            header = get_header(username=username, password=password, user_email=user_email, to_login=True)
            if header is not None:
                self.shared_data.header = header
                self.stacked_widget.setCurrentIndex(0)
            else:
                raise Exception
        except Exception:
            from IncorrectPassword import IncorrectPassword
            window = QtWidgets.QMainWindow()
            ui = IncorrectPassword()
            ui.setupUi(window)
            window.show()
=======
            header = get_header(username=username, password=password, user_email=user_email, to_login=True,
                                to_remember=False)
            if header.get("Authorization", None) is not None:
                with open("token", "w") as token_file:
                    token_file.write(header)
            else:
                self.logIn_button.clicked.connect(self.open_error)
            self.stacked_widget.setCurrentIndex(1)
        except Exception as e:
            self.logIn_button.clicked.connect(self.open_error)
>>>>>>> feature-setup-wizard

    def setup_ui(self, stacked_widget: QStackedWidget):
        """
        Sets up the user interface for the application.

        :param self: The instance of the class that this function belongs to.
        :param stacked_widget: QStackedWidget object representing the stacked widget to be used in the main window.
        :return: None
        """
        self.stacked_widget = stacked_widget

        self.setObjectName("self")
        self.resize(800, 600)

        font = QtGui.QFont()
        font.setPointSize(12)
        self.setFont(font)
        self.setStyleSheet("background-color: rgb(231, 255, 239);")

        self.central_widget = QtWidgets.QWidget(self)
        self.central_widget.setObjectName("centralwidget")

        self.LogIn = QtWidgets.QLabel(self.central_widget)
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

        self.username = QtWidgets.QLabel(self.central_widget)
        self.username.setGeometry(QtCore.QRect(300, 180, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.username.setFont(font)
        self.username.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                    "border-radius: 25px;")
        self.username.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.username.setObjectName("Username")

        self.password = QtWidgets.QLabel(self.central_widget)
        self.password.setGeometry(QtCore.QRect(300, 450, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.password.setFont(font)
        self.password.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                    "border-radius: 25px;")
        self.password.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.password.setObjectName("Password")

        self.log_in_button = QtWidgets.QPushButton(self.central_widget)
        self.log_in_button.setGeometry(QtCore.QRect(622, 517, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.log_in_button.setFont(font)
        self.log_in_button.setStyleSheet("""QPushButton:hover{background-color: rgb(235, 255, 197); 
                                                                    border: 1px solid black;
                                                                    border-radius: 25px;}
                                                                 QPushButton:!hover{background-color: rgb(235, 255, 197);
                                                                  border-radius: 25px;}
                                                                    """)
        self.log_in_button.setObjectName("logIn_button")

        self.username_input = QtWidgets.QLineEdit(self.central_widget)
        self.username_input.setGeometry(QtCore.QRect(310, 270, 181, 41))
        self.username_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.username_input.setObjectName("UsernameInput")

        self.password_input = QtWidgets.QLineEdit(self.central_widget)
        self.password_input.setGeometry(QtCore.QRect(310, 530, 181, 41))
        self.password_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.password_input.setObjectName("PasswordInput")

        self.back_btn = QtWidgets.QPushButton(self.central_widget)
        self.back_btn.setGeometry(QtCore.QRect(50, 517, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.back_btn.setFont(font)
        self.back_btn.setStyleSheet("""QPushButton:hover{background-color: rgb(235, 255, 197); 
                                                                    border: 1px solid black;
                                                                    border-radius: 25px;}
                                                                 QPushButton:!hover{background-color: rgb(235, 255, 197);
                                                                  border-radius: 25px;}
                                                                    """)
        self.back_btn.setObjectName("backbtn")

        self.email_lbl = QtWidgets.QLabel(self.central_widget)
        self.email_lbl.setGeometry(QtCore.QRect(300, 320, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.email_lbl.setFont(font)
        self.email_lbl.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                     "border-radius: 25px;")
        self.email_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.email_lbl.setObjectName("EmailLbl")

        self.email_txt = QtWidgets.QLineEdit(self.central_widget)
        self.email_txt.setGeometry(QtCore.QRect(310, 400, 181, 41))
        self.email_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.email_txt.setObjectName("EmailTxt")

        self.log_in_button.clicked.connect(self.log_in)
        self.log_in_button.clicked.connect(self.password_input.clear)
        self.log_in_button.clicked.connect(self.username_input.clear)
        self.log_in_button.clicked.connect(self.email_txt.clear)

        # was back
        self.back_btn.clicked.connect(self.open_main)

        self.retranslate_ui()
        stacked_widget.addWidget(self.central_widget)

    def retranslate_ui(self):
        """
        Retranslates the user interface elements.

        This function is responsible for updating the text of various user interface elements,
        such as window title, labels, buttons, etc., to the translated versions. It uses the
        `_translate` function from the `QtCore.QCoreApplication` module to perform the translation.

        :param self: The instance of the class that this method belongs to.
        :return: None
        """
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "MainWindow"))
        self.LogIn.setText(_translate("self", "Log in"))
        self.username.setText(_translate("self", "Username"))
        self.password.setText(_translate("self", "Password"))
        self.log_in_button.setText(_translate("self", "Log in"))
        self.back_btn.setText(_translate("self", "Back"))
        self.email_lbl.setText(_translate("self", "E-mail"))
