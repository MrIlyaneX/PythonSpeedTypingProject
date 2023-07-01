from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Rating(object):
    def Back(self):
        from MAIN_WINDOW import Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        # self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setToolTipDuration(108)
        MainWindow.setStyleSheet("background-color: rgb(231, 255, 239);\n"
"font: 12pt \"Arial Rounded MT Bold\";")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 181))
        self.frame.setStyleSheet(" background-color: rgb(194, 255, 172);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.RatingLbl = QtWidgets.QLabel(parent=self.frame)
        self.RatingLbl.setGeometry(QtCore.QRect(290, 60, 221, 71))
        self.RatingLbl.setStyleSheet("background-color: rgb(235, 255, 197);\n"
"border-radius: 25px;")
        self.RatingLbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.RatingLbl.setObjectName("RatingLbl")
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
        self.BackBtn.clicked.connect(MainWindow.close)
        self.scrollFast = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollFast.setGeometry(QtCore.QRect(100, 280, 241, 291))
        self.scrollFast.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scrollFast.setWidgetResizable(True)
        self.scrollFast.setObjectName("scrollFast")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 239, 289))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollFast.setWidget(self.scrollAreaWidgetContents)
        self.scrollDays = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollDays.setGeometry(QtCore.QRect(470, 280, 241, 291))
        self.scrollDays.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scrollDays.setWidgetResizable(True)
        self.scrollDays.setObjectName("scrollDays")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 239, 289))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollDays.setWidget(self.scrollAreaWidgetContents_2)
        self.TimeLbl = QtWidgets.QLabel(parent=self.centralwidget)
        self.TimeLbl.setGeometry(QtCore.QRect(70, 200, 301, 71))
        self.TimeLbl.setStyleSheet("background-color: rgb(235, 255, 197);\n"
"border-radius: 25px;")
        self.TimeLbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.TimeLbl.setObjectName("TimeLbl")
        self.DaysLbl = QtWidgets.QLabel(parent=self.centralwidget)
        self.DaysLbl.setGeometry(QtCore.QRect(440, 200, 301, 71))
        self.DaysLbl.setStyleSheet("background-color: rgb(235, 255, 197);\n"
"border-radius: 25px;")
        self.DaysLbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.DaysLbl.setObjectName("DaysLbl")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.RatingLbl.setText(_translate("MainWindow", "Rating"))
        self.BackBtn.setText(_translate("MainWindow", "Back"))
        self.TimeLbl.setText(_translate("MainWindow", "\"The fastest typers\""))
        self.DaysLbl.setText(_translate("MainWindow", "People that are with us"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Rating()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
