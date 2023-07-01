from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Achievements(object):
    def Back(self):
        from MAIN_WINDOW import Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        # self.window.show()

    def setupUi(self, Achievements):
        Achievements.setObjectName("Achievements")
        Achievements.resize(800, 600)
        Achievements.setStyleSheet("background-color: rgb(231, 255, 239);\n"
                                   "font: 12pt \"Arial Rounded MT Bold\";\n"
                                   "")
        self.centralwidget = QtWidgets.QWidget(parent=Achievements)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 800, 181))
        self.frame.setStyleSheet(" background-color: rgb(194, 255, 172);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.BackBtn = QtWidgets.QPushButton(parent=self.frame)
        self.BackBtn.setGeometry(QtCore.QRect(30, 20, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.BackBtn.setFont(font)
        self.BackBtn.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                   "border-radius: 15px;")
        self.BackBtn.setObjectName("BackBtn")
        # Button action to come back to the MainWindow
        self.BackBtn.clicked.connect(self.Back)
        self.BackBtn.clicked.connect(Achievements.close)

        self.AchievemjentsLbl = QtWidgets.QLabel(parent=self.frame)
        self.AchievemjentsLbl.setGeometry(QtCore.QRect(290, 40, 221, 81))
        self.AchievemjentsLbl.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                            "border-radius: 25px;")
        self.AchievemjentsLbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.AchievemjentsLbl.setObjectName("AchievemjentsLbl")
        self.scrollTime = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollTime.setGeometry(QtCore.QRect(100, 280, 241, 291))
        self.scrollTime.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scrollTime.setWidgetResizable(True)
        self.scrollTime.setObjectName("scrollTime")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 239, 289))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollTime.setWidget(self.scrollAreaWidgetContents)
        self.scrollDays = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollDays.setGeometry(QtCore.QRect(470, 280, 241, 291))
        self.scrollDays.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scrollDays.setWidgetResizable(True)
        self.scrollDays.setObjectName("scrollDays")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 239, 289))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollDays.setWidget(self.scrollAreaWidgetContents_2)
        self.BestTimeLbl = QtWidgets.QLabel(parent=self.centralwidget)
        self.BestTimeLbl.setGeometry(QtCore.QRect(70, 200, 301, 71))
        self.BestTimeLbl.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                       "border-radius: 25px;")
        self.BestTimeLbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.BestTimeLbl.setObjectName("BestTimeLbl")
        self.DaysWithUsLabl = QtWidgets.QLabel(parent=self.centralwidget)
        self.DaysWithUsLabl.setGeometry(QtCore.QRect(440, 200, 301, 71))
        self.DaysWithUsLabl.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                          "border-radius: 25px;")
        self.DaysWithUsLabl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.DaysWithUsLabl.setObjectName("DaysWithUsLabl")
        Achievements.setCentralWidget(self.centralwidget)

        self.retranslateUi(Achievements)
        QtCore.QMetaObject.connectSlotsByName(Achievements)

    def retranslateUi(self, Achievements):
        _translate = QtCore.QCoreApplication.translate
        Achievements.setWindowTitle(_translate("Achievements", "MainWindow"))
        self.BackBtn.setText(_translate("Achievements", "Back"))
        self.AchievemjentsLbl.setText(_translate("Achievements", "Achievements"))
        self.BestTimeLbl.setText(_translate("Achievements", "Your best time of typing"))
        self.DaysWithUsLabl.setText(_translate("Achievements", "Your days spent with us"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Achievements = QtWidgets.QMainWindow()
    ui = Ui_Achievements()
    ui.setupUi(Achievements)
    Achievements.show()
    sys.exit(app.exec())
