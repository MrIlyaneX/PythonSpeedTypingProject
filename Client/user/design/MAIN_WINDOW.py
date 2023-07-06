from PyQt6 import QtCore, QtGui, QtWidgets
from Account import Ui_Account
from Achievements import Ui_Achievements
from Rating import Ui_Rating
from Info import Ui_Info
from LogIn import Ui_LogIn


class Ui_MainWindow(object):
    def logIn(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_LogIn()
        self.ui.setupUi(self.window)
        # MainWindow.hide()
        self.window.show()

    def openInfo(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Info()
        self.ui.setupUi(self.window)
        # MainWindow.hide()
        self.window.show()

    def openRating(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Rating()
        self.ui.setupUi(self.window)
        # MainWindow.hide()
        self.window.show()

    def openAccount(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Account()
        self.ui.setupUi(self.window)
        # MainWindow.hide()
        self.window.show()

    def openAchievements(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Achievements()
        self.ui.setupUi(self.window)
        # MainWindow.hide()
        self.window.show()

    def startAgain(self):
        # self.window = QtWidgets.QMainWindow()
        # self.ui = Ui_Achievements()
        # self.ui.setupUi(self.window)
        self.our_text_for_typing.clear()
        self.User_text.clear()
        self.displayText("Hello!")
        # self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(231, 255, 239);\n"
                                 "font: 12pt \"Arial Rounded MT Bold\";")
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Try_your_speedLbl = QtWidgets.QLabel(parent=self.centralwidget)
        self.Try_your_speedLbl.setGeometry(QtCore.QRect(270, 210, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.Try_your_speedLbl.setFont(font)
        self.Try_your_speedLbl.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                             "border-radius: 25px;")
        self.Try_your_speedLbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Try_your_speedLbl.setObjectName("Try_your_speedLbl")
        self.our_text_for_typing = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.our_text_for_typing.setGeometry(QtCore.QRect(110, 290, 591, 221))
        self.our_text_for_typing.setStyleSheet("background-color: rgb(255, 255, 255);"
                                               "border: none;\n"
                                               "color:gray;"
                                               "font-size:16px;")
        # self.our_text_for_typing.setPlaceholderText("Message")
        self.our_text_for_typing.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop)
        self.our_text_for_typing.setObjectName("our_text_for_typing")
        self.User_text = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.User_text.setGeometry(QtCore.QRect(112, 293, 591, 221))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.User_text.sizePolicy().hasHeightForWidth())
        self.User_text.setSizePolicy(sizePolicy)
        self.User_text.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                     "border: none;\n"
                                     "font-size:16px;\n"
                                     )
        self.User_text.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop)
        self.User_text.setObjectName("User_text")
        self.User_text.setGraphicsEffect(QtWidgets.QGraphicsOpacityEffect())
        self.User_text.textChanged.connect(self.onTextChanged)
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 181))
        self.frame.setStyleSheet(" background-color: rgb(194, 255, 172);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.accountBtn = QtWidgets.QPushButton(parent=self.frame)
        self.accountBtn.setGeometry(QtCore.QRect(30, 10, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.accountBtn.setFont(font)
        self.accountBtn.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                      "border-radius: 25px;")
        self.accountBtn.setObjectName("accountBtn")
        self.accountBtn.clicked.connect(self.openAccount)
        self.accountBtn.setAutoDefault(False)
        self.RatingBtn = QtWidgets.QPushButton(parent=self.frame)
        self.RatingBtn.setGeometry(QtCore.QRect(320, 10, 171, 61))
        self.RatingBtn.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                     "border-radius: 25px;")
        self.RatingBtn.setObjectName("RatingBtn")
        self.RatingBtn.clicked.connect(self.openRating)
        self.RatingBtn.setAutoDefault(False)
        self.SettingsBtn = QtWidgets.QPushButton(parent=self.frame)
        self.SettingsBtn.setGeometry(QtCore.QRect(610, 10, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.SettingsBtn.setFont(font)
        self.SettingsBtn.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                       "border-radius: 25px;")
        self.SettingsBtn.setObjectName("SettingsBtn")
        self.InfoBtn = QtWidgets.QPushButton(parent=self.frame)
        self.InfoBtn.setGeometry(QtCore.QRect(470, 90, 171, 61))
        self.InfoBtn.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                   "border-radius: 25px;")
        self.InfoBtn.setObjectName("InfoBtn")
        self.InfoBtn.clicked.connect(self.openInfo)
        self.InfoBtn.setAutoDefault(False)
        self.achievementsBtn = QtWidgets.QPushButton(parent=self.frame)
        self.achievementsBtn.setGeometry(QtCore.QRect(180, 90, 171, 61))
        self.achievementsBtn.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                           "border-radius: 25px;")
        self.achievementsBtn.setObjectName("achievementsBtn")
        self.achievementsBtn.clicked.connect(self.openAchievements)
        self.achievementsBtn.setAutoDefault(False)
        self.Start_againBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Start_againBtn.setGeometry(QtCore.QRect(650, 550, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.Start_againBtn.setFont(font)
        self.Start_againBtn.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                          "border-radius: 15px;")
        self.Start_againBtn.setObjectName("Start_againBtn")
        self.LogInBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.LogInBtn.setGeometry(QtCore.QRect(20, 550, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.LogInBtn.setFont(font)
        self.LogInBtn.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                    "border-radius: 15px;")
        self.LogInBtn.setObjectName("LogInBtn")
        self.LogInBtn.clicked.connect(self.logIn)
        self.LogInBtn.setAutoDefault(False)
        self.Start_againBtn.clicked.connect(self.startAgain)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Try_your_speedLbl.setText(_translate("MainWindow", "Try your speed typing"))
        self.accountBtn.setText(_translate("MainWindow", "Account"))
        self.RatingBtn.setText(_translate("MainWindow", "Rating"))
        self.SettingsBtn.setText(_translate("MainWindow", "Settings"))
        self.InfoBtn.setText(_translate("MainWindow", "Information"))
        self.achievementsBtn.setText(_translate("MainWindow", "Achievements"))
        self.Start_againBtn.setText(_translate("MainWindow", "Start again"))
        self.LogInBtn.setText(_translate("MainWindow", "LogIn"))

    # This function adds the text to display for users typing
    def displayText(self, text):
        self.our_text_for_typing.setText(text)

    # def onTextChanged(self, text):
    #     self.our_text_for_typing.setText(text)

    # def onTextChanged(self, text):
    #     self.our_text_for_typing.clear()  # Clear the existing text in our_text_for_typing
    #
    #     # Show only the symbols in User_text that are not present in our_text_for_typing
    #     user_text = self.User_text.text()
    #     diff_text = user_text[len(self.our_text_for_typing.toPlainText()):]
    #     self.our_text_for_typing.append(diff_text)

    def onTextChanged(self, text):
        user_text = self.User_text.text()
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

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.displayText("Hello my name is Polina!! I'm 5 years old")
    MainWindow.show()
    sys.exit(app.exec())
