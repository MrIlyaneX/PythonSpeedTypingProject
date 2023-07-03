from PyQt6 import QtCore, QtGui, QtWidgets
from Account import Ui_Account
from Achievements import Ui_Achievements
from Rating import Ui_Rating
from Info import Ui_Info
from LogIn import Ui_LogIn


class Ui_MainWindow(object):
    def log_in(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_LogIn()
        self.ui.setup_ui(self.window)
        # MainWindow.hide()
        self.window.show()

    def open_info(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Info()
        self.ui.setup_ui(self.window)
        # MainWindow.hide()
        self.window.show()

    def open_rating(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Rating()
        self.ui.setup_ui(self.window)
        # MainWindow.hide()
        self.window.show()

    def open_account(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Account()
        self.ui.setup_ui(self.window)
        # MainWindow.hide()
        self.window.show()

    def open_achievements(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Achievements()
        self.ui.setup_ui(self.window)
        # MainWindow.hide()
        self.window.show()

    def setup_ui(self, MainWindow):
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
        self.our_text_for_typing.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.our_text_for_typing.setObjectName("our_text_for_typing")
        self.User_text = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.User_text.setGeometry(QtCore.QRect(110, 290, 591, 221))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.User_text.sizePolicy().hasHeightForWidth())
        self.User_text.setSizePolicy(sizePolicy)
        self.User_text.setStyleSheet("background-color: rgb(255, 255, 255, 0);\n"
                                     "border: none;")
        self.User_text.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop)
        self.User_text.setObjectName("User_text")
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
        self.accountBtn.clicked.connect(self.open_account)
        self.accountBtn.setAutoDefault(False)
        self.RatingBtn = QtWidgets.QPushButton(parent=self.frame)
        self.RatingBtn.setGeometry(QtCore.QRect(320, 10, 171, 61))
        self.RatingBtn.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                     "border-radius: 25px;")
        self.RatingBtn.setObjectName("RatingBtn")
        self.RatingBtn.clicked.connect(self.open_rating)
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
        self.InfoBtn.clicked.connect(self.open_info)
        self.InfoBtn.setAutoDefault(False)
        self.achievementsBtn = QtWidgets.QPushButton(parent=self.frame)
        self.achievementsBtn.setGeometry(QtCore.QRect(180, 90, 171, 61))
        self.achievementsBtn.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                           "border-radius: 25px;")
        self.achievementsBtn.setObjectName("achievementsBtn")
        self.achievementsBtn.clicked.connect(self.open_achievements)
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
        self.LogInBtn.clicked.connect(self.log_in)
        self.LogInBtn.setAutoDefault(False)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Try_your_speedLbl.setText(_translate("MainWindow", "Try your speed typing"))
        self.our_text_for_typing.setHtml(_translate("MainWindow",
                                                    "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                    "p, li { white-space: pre-wrap; }\n"
                                                    "</style></head><body style=\" font-family:\'Arial Rounded MT Bold\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                                    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Verdana,Geneva,sans-serif\'; color:#b8b8b8; background-color:#ffffff;\">Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo</span></p></body></html>"))
        self.accountBtn.setText(_translate("MainWindow", "Account"))
        self.RatingBtn.setText(_translate("MainWindow", "Rating"))
        self.SettingsBtn.setText(_translate("MainWindow", "Settings"))
        self.InfoBtn.setText(_translate("MainWindow", "Information"))
        self.achievementsBtn.setText(_translate("MainWindow", "Achievements"))
        self.Start_againBtn.setText(_translate("MainWindow", "Start again"))
        self.LogInBtn.setText(_translate("MainWindow", "LogIn"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setup_ui(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
