import traceback

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QStackedWidget
from PyQt6.QtWidgets import QWidget as QWidget

<<<<<<< HEAD
from Client import SharedData
from Client.user.design.SameUsername import SameUsernameWindow
=======
>>>>>>> feature-setup-wizard
from Client.client_runner import get_header


class CreateAccountWindow(QWidget):
    def __init__(self, shared_data: SharedData):
        super().__init__()
        self.shared_data = shared_data
        self.error_window = None
        self.error_ui = None

    def open_main(self):
        """
        Opens the initial window by setting the current index of the stacked widget to 0.

        :param self: The instance of the class that this method belongs to.
        :return: None
        """
        self.stacked_widget.setCurrentIndex(0)

    def get_username(self):
        """
        Retrieves the username entered by the user.
        This function retrieves the text entered the username_input QLineEdit widget, which is
        assumed to be a username provided by the user.

        :param self: The instance of the class that this method belongs to.
        :return: The username entered by the user as a string.
        """
        return self.name_text.text()

    def get_password(self):
        """
        Retrieves the password entered by the user.
        This function retrieves the text entered the password_input QLineEdit widget, which is
        assumed to be a username provided by the user.

        :param self: The instance of the class that this method belongs to.
        :return: The password entered by the user as a string.
        """
        return self.password_text.text()

    def get_email(self):
        """
        Retrieves the email entered by the user.
        This function retrieves the text entered the email_txt QLineEdit widget, which is
        assumed to be a username provided by the user.

        :param self: The instance of the class that this method belongs to.
        :return: The password entered by the user as a string.
        """
        return self.email_text.text()

    def button_clicked(self):
        """
        Registers the user using the collected information when the 'sign_up' button is clicked.

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
        user_email = self.get_email()
        username = self.get_username()
        password = self.get_password()
        try:
            header = get_header(username=username, password=password, user_email=user_email, to_signup=True)
            print(header)
            if header.get("Authorization", None) is None:
                self.shared_data.header = header
                self.stacked_widget.setCurrentIndex(0)
            else:
                print("Here")

        except Exception as e:
            traceback.print_exc()
            self.show_error_window()

    def show_error_window(self):
        if self.error_window is None:
            self.error_window = QtWidgets.QMainWindow()
            self.error_ui = SameUsernameWindow()
            self.error_ui.setup_ui()
            self.error_window.setCentralWidget(self.error_ui)
        self.error_window.show()

    def setup_ui(self, stacked_widget: QStackedWidget):
        """
        Sets up the user interface for the main window.

        :param self: The instance of the class that this function belongs to.
        :return: None
        """
        self.stacked_widget = stacked_widget
        self.setObjectName("self")
        self.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.setFont(font)
        self.setStyleSheet("background-color: rgb(231, 255, 239);")

        self.central_widget = QtWidgets.QWidget(self)
        self.central_widget.setObjectName("centralwidget")

        self.create_account = QtWidgets.QLabel(self.central_widget)
        self.create_account.setGeometry(QtCore.QRect(0, 0, 801, 181))
        self.create_account.setMinimumSize(QtCore.QSize(0, 181))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(16)
        self.create_account.setFont(font)
        self.create_account.setStyleSheet("background-color: rgb(194, 255, 172);")
        self.create_account.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.create_account.setObjectName("create_account")

        self.write_your_name_lbl = QtWidgets.QLabel(self.central_widget)
        self.write_your_name_lbl.setGeometry(QtCore.QRect(290, 190, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.write_your_name_lbl.setFont(font)
        self.write_your_name_lbl.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                               "border-radius: 25px;")
        self.write_your_name_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.write_your_name_lbl.setObjectName("write_your_name_lbl")

        self.create_a_password_lbl = QtWidgets.QLabel(self.central_widget)
        self.create_a_password_lbl.setGeometry(QtCore.QRect(290, 460, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.create_a_password_lbl.setFont(font)
        self.create_a_password_lbl.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                                 "border-radius: 25px;")
        self.create_a_password_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.create_a_password_lbl.setObjectName("create_a_password_lbl")

        self.name_text = QtWidgets.QLineEdit(self.central_widget)
        self.name_text.setGeometry(QtCore.QRect(300, 270, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.name_text.setFont(font)
        self.name_text.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.name_text.setObjectName("name_text")

        self.password_text = QtWidgets.QLineEdit(self.central_widget)
        self.password_text.setGeometry(QtCore.QRect(300, 540, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.password_text.setFont(font)
        self.password_text.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.password_text.setObjectName("password_text")

        self.save_btn = QtWidgets.QPushButton(self.central_widget)
        self.save_btn.setGeometry(QtCore.QRect(622, 517, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.save_btn.setFont(font)
        self.save_btn.setStyleSheet("""QPushButton:hover{background-color: rgb(235, 255, 197); 
                                                                    border: 1px solid black;
                                                                    border-radius: 25px;}
                                                                 QPushButton:!hover{background-color: rgb(235, 255, 197);
                                                                  border-radius: 25px;}
                                                                    """)
        self.save_btn.setObjectName("save_btn")

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
        self.back_btn.setObjectName("back_btn")
        self.back_btn.clicked.connect(self.open_main)

        self.email_text = QtWidgets.QLineEdit(self.central_widget)
        self.email_text.setGeometry(QtCore.QRect(300, 400, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.email_text.setFont(font)
        self.email_text.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.email_text.setObjectName("email_text")

        self.email_lbl = QtWidgets.QLabel(self.central_widget)
        self.email_lbl.setGeometry(QtCore.QRect(290, 320, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.email_lbl.setFont(font)
        self.email_lbl.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                     "border-radius: 25px;")
        self.email_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.email_lbl.setObjectName("email_lbl")

        self.save_btn.clicked.connect(self.button_clicked)
        self.save_btn.clicked.connect(self.password_text.clear)
        self.save_btn.clicked.connect(self.name_text.clear)
        self.save_btn.clicked.connect(self.email_text.clear)

        self.retranslate_ui()
        stacked_widget.addWidget(self.central_widget)

    def retranslate_ui(self):
        """
        This function sets the translated text for various UI elements in the main window.

        :return: None
        """
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.create_account.setText(_translate("self", "Create an account"))
        self.write_your_name_lbl.setText(_translate("self", "Write you name"))
        self.create_a_password_lbl.setText(_translate("self", "Create a password"))
        self.save_btn.setText(_translate("self", "Save"))
        self.back_btn.setText(_translate("self", "Back"))
        self.email_lbl.setText(_translate("self", "Write your e-mail"))
