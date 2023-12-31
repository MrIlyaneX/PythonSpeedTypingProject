import time
import traceback

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QStackedWidget
from PyQt6.QtWidgets import QWidget as QWidget

from Client import SharedData
from Client.user.scripts.text_generator import generate_text


class MainWindow(QWidget):
    """
    This class is responsible for the user interface of the main window.
    """
    def __init__(self, shared_data: SharedData):
        """
        Initializes the MainWindow class.
        """
        super().__init__()
        self.start_time = time.time()
        self.end_time = None
        self.typing_time = None
        self.shared_data = shared_data

    def open_login(self):
        """
        Opens the initial window by setting the current index of the stacked widget to 0.

        :param self: The instance of the class that this function belongs to.
        :return: None
        """

        self.shared_data.update_windows()
        self.stacked_widget.setCurrentIndex(0)

    def open_info(self):
        """
        Opens the window with info about the project by setting the current index of the stacked widget to 3

        :param self: The instance of the class that this function belongs to.
        :return: None
        """

        self.shared_data.update_windows()
        self.stacked_widget.setCurrentIndex(3)

    def open_account(self):
        """
        Opens the window with information about the user by setting the current index of the stacked widget to 5

        :param self: The instance of the class that this function belongs to.
        :return: None
        """

        self.shared_data.update_windows()
        self.stacked_widget.setCurrentIndex(5)

    def open_achievements(self):
        """
        Opens the window with information about the user's achievements by setting the current index of the stacked
        widget to 6

        :param self: The instance of the class that this function belongs to.
        :return: None
        """

        self.shared_data.update_windows()
        self.stacked_widget.setCurrentIndex(6)

    def open_rating(self):
        """
        Opens the window with user's rating by setting the current index of the stacked widget to 7

        :param self: The instance of the class that this function belongs to.
        :return: None
        """

        self.shared_data.update_windows()
        self.stacked_widget.setCurrentIndex(7)

    def start_again(self):
        """
        This function allows the user to erase their input and start again. It Clears the text in the
        'our_text_for_typing' input field and in the 'user_text' input field.

        :param self: The instance of the class that this function belongs to.
        :return: None
        """

        self.typingAccuracy()
        if self.start_time is not None:
            self.typing_time = time.time() - self.start_time
        self.typingSpeed()
        try:
            self.shared_data.upload_info_on_server()
        except Exception as e:
            traceback.print_exc()
        self.start_time = None
        self.our_text_for_typing.clear()
        self.user_text.clear()
        text = generate_text()
        display = ""
        for i in range(len(text)):
            display += text[i]
        self.display_text(display)

    def display_text(self, text):
        """
        This function sets the text to be displayed for the user's typing. Function sets the text of the
        'our_text_for_typing' widget to the provided text.

        :param self: The instance of the class that this function belongs to.
        :param text: The text to be displayed for the user's typing.
        :return: None
        """
        self.our_text_for_typing.setText(text)

    def on_text_changed(self):
        """
        This function updates the text display based on the user's input. It updates the text display of the
        'our_text_for_typing' widget with color highlighting.

        :param self: The instance of the class that this function belongs to.
        :return: None
        """
        if self.start_time is None:
            self.start_time = time.time()
        user_text = self.user_text.toPlainText()
        user_text_length = len(user_text)
        our_text = self.our_text_for_typing.toPlainText()
        colored_text = ""

        for i in range(len(our_text)):
            if i < user_text_length:
                # Set color for matched character
                colored_text += f"<font color='white'>{our_text[i]}</font>"
                # colored_text += f"<font color='white'>{user_text[i]}</font>"
            else:
                # Set default color for remaining characters
                colored_text += our_text[i]

        self.our_text_for_typing.setHtml(colored_text)

    def typingAccuracy(self):
        """
        Counts the accuracy of typing
        """
        userText = self.user_text.toPlainText()
        ourText = self.our_text_for_typing.toPlainText()
        if len(userText) == 0:
            return 0
        if len(userText) < len(ourText):
            length = len(userText)
        else:
            length = len(ourText)
        matchCount = 0
        for i in range(length):
            if userText[i] == ourText[i]:
                matchCount += 1

        accuracy = int(matchCount / len(ourText) * 100)
        print("Accuracy: ", accuracy)
        self.shared_data.update_accuracy(accuracy=accuracy)

    def typingSpeed(self):
        """
        Counts the speed of typing 10 symbols
        """
        if len(self.user_text.toPlainText()) == 0:
            # print("No words")
            return 0
        else:
            a = int(self.typing_time / len(self.user_text.toPlainText()) * 10)
            print("Time: ", a)
            self.shared_data.update_score(a)

    def setup_ui(self, stacked_widget: QStackedWidget):
        """
        Sets up the user interface for the main window.

        :param self: The instance of the class that this function belongs to.
        :param stacked_widget: QStackedWidget object representing the stacked widget to be used in the main window.
        :return: None
        """
        # self.start_time = time.time()
        self.stacked_widget = stacked_widget
        self.stacked_widget.setWindowTitle("Speed-typing app")
        self.setObjectName("MainWindow")
        self.setEnabled(True)
        self.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.setFont(font)
        self.setStyleSheet("background-color: rgb(231, 255, 239);\n"
                           "font: 12pt \"Arial Rounded MT Bold\";")

        self.central_widget = QtWidgets.QWidget(parent=self)
        self.central_widget.setObjectName("central_widget")

        self.try_your_speed_lbl = QtWidgets.QLabel(parent=self.central_widget)
        self.try_your_speed_lbl.setGeometry(QtCore.QRect(270, 210, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.try_your_speed_lbl.setFont(font)
        self.try_your_speed_lbl.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                              "border-radius: 25px;")
        self.try_your_speed_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.try_your_speed_lbl.setObjectName("try_your_speed_lbl")

        self.our_text_for_typing = QtWidgets.QTextBrowser(parent=self.central_widget)
        self.our_text_for_typing.setGeometry(QtCore.QRect(110, 290, 591, 221))
        self.our_text_for_typing.setStyleSheet("background-color: rgb(255, 255, 255);"
                                               "border: none;\n"
                                               "color:gray;"
                                               "font-size:16px;")
        self.our_text_for_typing.setObjectName("our_text_for_typing")
        self.our_text_for_typing.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop)
        self.frame = QtWidgets.QFrame(parent=self.central_widget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 181))
        self.frame.setStyleSheet(" background-color: rgb(194, 255, 172);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")

        self.account_btn = QtWidgets.QPushButton(parent=self.frame)
        self.account_btn.setGeometry(QtCore.QRect(30, 10, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.account_btn.setFont(font)
        self.account_btn.setStyleSheet("""QPushButton:hover{background-color: rgb(235, 255, 197); 
                                                            border: 1px solid black;
                                                            border-radius: 25px;}
                                                         QPushButton:!hover{background-color: rgb(235, 255, 197);
                                                          border-radius: 25px;}
                                                            """)
        self.account_btn.setObjectName("account_btn")
        self.account_btn.clicked.connect(self.open_account)
        self.account_btn.setAutoDefault(False)

        self.rating_btn = QtWidgets.QPushButton(parent=self.frame)
        self.rating_btn.setGeometry(QtCore.QRect(320, 10, 171, 61))
        self.rating_btn.setStyleSheet("""QPushButton:hover{background-color: rgb(235, 255, 197); 
                                                            border: 1px solid black;
                                                            border-radius: 25px;}
                                                         QPushButton:!hover{background-color: rgb(235, 255, 197);
                                                          border-radius: 25px;}
                                                            """)
        self.rating_btn.setObjectName("rating_btn")
        self.rating_btn.clicked.connect(self.open_rating)
        self.rating_btn.setAutoDefault(False)

        self.settings_btn = QtWidgets.QPushButton(parent=self.frame)
        self.settings_btn.setGeometry(QtCore.QRect(610, 10, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.settings_btn.setFont(font)
        self.settings_btn.setStyleSheet("""QPushButton:hover{background-color: rgb(235, 255, 197); 
                                                            border: 1px solid black;
                                                            border-radius: 25px;}
                                                         QPushButton:!hover{background-color: rgb(235, 255, 197);
                                                          border-radius: 25px;}
                                                            """)
        self.settings_btn.setObjectName("settings_btn")

        self.info_btn = QtWidgets.QPushButton(parent=self.frame)
        self.info_btn.setGeometry(QtCore.QRect(470, 90, 171, 61))
        self.info_btn.setStyleSheet("""QPushButton:hover{background-color: rgb(235, 255, 197); 
                                                            border: 1px solid black;
                                                            border-radius: 25px;}
                                                         QPushButton:!hover{background-color: rgb(235, 255, 197);
                                                          border-radius: 25px;}
                                                            """)
        self.info_btn.setObjectName("info_btn")
        self.info_btn.clicked.connect(self.open_info)
        self.info_btn.setAutoDefault(False)

        self.achievements_btn = QtWidgets.QPushButton(parent=self.frame)
        self.achievements_btn.setGeometry(QtCore.QRect(180, 90, 171, 61))
        self.achievements_btn.setStyleSheet("""QPushButton:hover{background-color: rgb(235, 255, 197); 
                                                            border: 1px solid black;
                                                            border-radius: 25px;}
                                                         QPushButton:!hover{background-color: rgb(235, 255, 197);
                                                          border-radius: 25px;}
                                                            """)
        self.achievements_btn.setObjectName("achievements_btn")
        self.achievements_btn.clicked.connect(self.open_achievements)
        self.achievements_btn.setAutoDefault(False)

        self.start_again_btn = QtWidgets.QPushButton(parent=self.central_widget)
        self.start_again_btn.setGeometry(QtCore.QRect(650, 550, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.start_again_btn.setFont(font)
        self.start_again_btn.setStyleSheet("""QPushButton:hover{background-color: rgb(235, 255, 197); 
                                                            border: 1px solid black;
                                                            border-radius: 15px;}
                                                         QPushButton:!hover{background-color: rgb(235, 255, 197);
                                                          border-radius: 15px;}
                                                            """)
        self.start_again_btn.clicked.connect(self.start_again)
        self.start_again_btn.setAutoDefault(False)
        self.start_again_btn.setObjectName("start_again_btn")
        self.log_in_btn = QtWidgets.QPushButton(parent=self.central_widget)
        self.log_in_btn.setGeometry(QtCore.QRect(20, 550, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.log_in_btn.setFont(font)
        self.log_in_btn.setStyleSheet("""QPushButton:hover{background-color: rgb(235, 255, 197); 
                                                            border: 1px solid black;
                                                            border-radius: 15px;}
                                                         QPushButton:!hover{background-color: rgb(235, 255, 197);
                                                          border-radius: 15px;}
                                                            """)
        self.log_in_btn.setObjectName("log_in_btn")
        self.log_in_btn.clicked.connect(self.open_login)
        self.log_in_btn.setAutoDefault(False)

        self.user_text = QtWidgets.QTextEdit(parent=self.central_widget)
        self.user_text.setGeometry(QtCore.QRect(110, 290, 591, 221))
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.user_text.setFont(font)
        self.user_text.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                     "border: none;\n"
                                     "color:black;"
                                     "font-size:16px;\n")
        self.user_text.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop)
        self.user_text.setObjectName("user_text")
        self.user_text.textChanged.connect(self.on_text_changed)

        self.try_your_speed_lbl.raise_()
        self.our_text_for_typing.raise_()
        self.user_text.raise_()
        self.frame.raise_()
        self.start_again_btn.raise_()
        self.log_in_btn.raise_()

        self.retranslate_ui(self)
        stacked_widget.addWidget(self.central_widget)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslate_ui(self, main_window):
        """
        This function sets the translated text for various UI elements in the main window.
        :return: None
        """
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.try_your_speed_lbl.setText(_translate("MainWindow", "Try your speed"))
        self.account_btn.setText(_translate("MainWindow", "Account"))
        self.rating_btn.setText(_translate("MainWindow", "Rating"))
        self.settings_btn.setText(_translate("MainWindow", "Settings"))
        self.info_btn.setText(_translate("MainWindow", "Info"))
        self.achievements_btn.setText(_translate("MainWindow", "Achievements"))
        self.start_again_btn.setText(_translate("MainWindow", "Start again"))
        self.log_in_btn.setText(_translate("MainWindow", "Log in"))
