# Form implementation generated from reading ui file 'MAIN_WINDOW.ui'
#
# Created by: PyQt6 UI code generator 6.4.2

from PyQt6 import QtCore, QtGui, QtWidgets
from Account import Ui_Account
from Achievements import Ui_Achievements
from Rating import Ui_Rating
from Info import Ui_Back

class Ui_MainWindow1(object):
    def openInfo(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Back()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()

    def openRating(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Rating()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()

    def openAccount(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Account()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()

    def openAchievements(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Achievements()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()

    def setupUi(self, MainWindow1):
        MainWindow1.setObjectName("MainWindow1")
        MainWindow1.setEnabled(True)
        MainWindow1.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        MainWindow1.setFont(font)
        MainWindow1.setStyleSheet("background-color: rgb(231, 255, 239);\n"
"font: 12pt \"Arial Rounded MT Bold\";")
        MainWindow1.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow1)
        self.centralwidget.setObjectName("centralwidget")
        self.Try_your_speed = QtWidgets.QLabel(parent=self.centralwidget)
        self.Try_your_speed.setGeometry(QtCore.QRect(270, 200, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.Try_your_speed.setFont(font)
        self.Try_your_speed.setStyleSheet("background-color: rgb(235, 255, 197);\n"
"border-radius: 25px;")
        self.Try_your_speed.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Try_your_speed.setObjectName("Try_your_speed")
        self.progressBar = QtWidgets.QProgressBar(parent=self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(220, 270, 381, 23))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 50)
        self.progressBar.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.our_text_for_typing = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.our_text_for_typing.setGeometry(QtCore.QRect(110, 310, 591, 221))
        self.our_text_for_typing.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.our_text_for_typing.setObjectName("our_text_for_typing")
        self.User_text = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.User_text.setGeometry(QtCore.QRect(110, 310, 591, 221))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.User_text.sizePolicy().hasHeightForWidth())
        self.User_text.setSizePolicy(sizePolicy)
        self.User_text.setStyleSheet("background-color: rgb(255, 255, 255, 0);\n"
"border: none;")
        self.User_text.setObjectName("User_text")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 181))
        self.frame.setStyleSheet(" background-color: rgb(194, 255, 172);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.account = QtWidgets.QPushButton(parent=self.frame)
        self.account.setGeometry(QtCore.QRect(30, 10, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.account.setFont(font)
        self.account.setStyleSheet("background-color: rgb(235, 255, 197);\n"
"border-radius: 25px;")
        self.account.setObjectName("account")

        self.account.clicked.connect(self.openAccount)

        self.Rating = QtWidgets.QPushButton(parent=self.frame)
        self.Rating.setGeometry(QtCore.QRect(320, 10, 171, 61))
        self.Rating.setStyleSheet("background-color: rgb(235, 255, 197);\n"
"border-radius: 25px;")
        self.Rating.setObjectName("Rating")
        self.Rating.clicked.connect(self.openRating)
        self.Settings = QtWidgets.QPushButton(parent=self.frame)
        self.Settings.setGeometry(QtCore.QRect(610, 10, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Settings.setFont(font)
        self.Settings.setStyleSheet("background-color: rgb(235, 255, 197);\n"
"border-radius: 25px;")
        self.Settings.setObjectName("Settings")
        self.Info = QtWidgets.QPushButton(parent=self.frame)
        self.Info.setGeometry(QtCore.QRect(470, 90, 171, 61))
        self.Info.setStyleSheet("background-color: rgb(235, 255, 197);\n"
"border-radius: 25px;")
        self.Info.setObjectName("Info")
        self.Info.clicked.connect(self.openInfo)
        self.achievements = QtWidgets.QPushButton(parent=self.frame)
        self.achievements.setGeometry(QtCore.QRect(180, 90, 171, 61))
        self.achievements.setStyleSheet("background-color: rgb(235, 255, 197);\n"
"border-radius: 25px;")
        self.achievements.setObjectName("achievements")
        self.achievements.clicked.connect(self.openAchievements)
        self.Start_again = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Start_again.setGeometry(QtCore.QRect(650, 550, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.Start_again.setFont(font)
        self.Start_again.setStyleSheet("background-color: rgb(235, 255, 197);\n"
"border-radius: 25px;")
        self.Start_again.setObjectName("Start_again")
        MainWindow1.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow1)

    def retranslateUi(self, MainWindow1):
        _translate = QtCore.QCoreApplication.translate
        MainWindow1.setWindowTitle(_translate("MainWindow1", "MainWindow1"))
        self.Try_your_speed.setText(_translate("MainWindow1", "Try your speed typing"))
        self.account.setText(_translate("MainWindow1", "Account"))
        self.Rating.setText(_translate("MainWindow1", "Rating"))
        self.Settings.setText(_translate("MainWindow1", "Settings"))
        self.Info.setText(_translate("MainWindow1", "Information"))
        self.achievements.setText(_translate("MainWindow1", "Achievements"))
        self.Start_again.setText(_translate("MainWindow1", "Start again"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
