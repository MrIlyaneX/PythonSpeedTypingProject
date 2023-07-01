from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Info(object):
    def Back(self):
        from MAIN_WINDOW import Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)


    def setupUi(self, Back):
        Back.setObjectName("Back")
        Back.resize(800, 600)
        Back.setStyleSheet("background-color: rgb(231, 255, 239);\n"
                           "font: 12pt \"Arial Rounded MT Bold\";")
        self.centralwidget = QtWidgets.QWidget(parent=Back)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 181))
        self.frame.setStyleSheet(" background-color: rgb(194, 255, 172);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.InfoLbl = QtWidgets.QLabel(parent=self.frame)
        self.InfoLbl.setGeometry(QtCore.QRect(300, 60, 201, 71))
        self.InfoLbl.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                   "border-radius: 25px;")
        self.InfoLbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.InfoLbl.setObjectName("InfoLbl")
        self.backBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.backBtn.setGeometry(QtCore.QRect(610, 520, 171, 61))
        self.backBtn.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                   "border-radius: 25px;")
        self.backBtn.setObjectName("backBtn")
        # Button action to come back to the MainWindow
        self.backBtn.clicked.connect(self.Back)
        self.backBtn.clicked.connect(Back.close)
        self.DescriptionText = QtWidgets.QLabel(parent=self.centralwidget)
        self.DescriptionText.setGeometry(QtCore.QRect(60, 230, 671, 241))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.DescriptionText.setFont(font)
        self.DescriptionText.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                           "border-radius: 25px;\n"
                                           "\n"
                                           "\n"
                                           "")
        self.DescriptionText.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.DescriptionText.setWordWrap(True)
        self.DescriptionText.setObjectName("DescriptionText")
        Back.setCentralWidget(self.centralwidget)

        self.retranslateUi(Back)
        QtCore.QMetaObject.connectSlotsByName(Back)

    def retranslateUi(self, Back):
        _translate = QtCore.QCoreApplication.translate
        Back.setWindowTitle(_translate("Back", "MainWindow"))
        self.InfoLbl.setText(_translate("Back", "Information"))
        self.backBtn.setText(_translate("Back", "Back"))
        self.DescriptionText.setText(_translate("Back",
                                                "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#262626;\">Our typing speed application project is designed for entertainment purposes, without a strong scientific focus. While similar resources already exist on the Internet, they are often imperfect, with users complaining about limited functionality, excessive advertising, a complex interface, and inflexible settings.</span></p></body></html>"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Info()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
