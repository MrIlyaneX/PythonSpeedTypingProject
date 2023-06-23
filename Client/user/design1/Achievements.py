# Form implementation generated from reading ui file 'Achievements.ui'
#
# Created by: PyQt6 UI code generator 6.5.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Achievements(object):
    def setupUi(self, Achievements):
        Achievements.setObjectName("Achievements")
        Achievements.resize(800, 600)
        Achievements.setStyleSheet("background-color: rgb(231, 255, 239);\n"
"font: 12pt \"Arial Rounded MT Bold\";\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=Achievements)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 181))
        self.frame.setStyleSheet(" background-color: rgb(194, 255, 172);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.Achievements_2 = QtWidgets.QPushButton(parent=self.frame)
        self.Achievements_2.setGeometry(QtCore.QRect(290, 40, 221, 81))
        self.Achievements_2.setStyleSheet("background-color: rgb(235, 255, 197);\n"
"border-radius: 25px;")
        self.Achievements_2.setObjectName("Achievements_2")
        self.DaysWithUs = QtWidgets.QPushButton(parent=self.centralwidget)
        self.DaysWithUs.setGeometry(QtCore.QRect(440, 200, 301, 71))
        self.DaysWithUs.setStyleSheet("background-color: rgb(235, 255, 197);\n"
"border-radius: 25px;")
        self.DaysWithUs.setObjectName("DaysWithUs")
        self.BestTime = QtWidgets.QPushButton(parent=self.centralwidget)
        self.BestTime.setGeometry(QtCore.QRect(70, 200, 301, 71))
        self.BestTime.setStyleSheet("background-color: rgb(235, 255, 197);\n"
"border-radius: 25px;")
        self.BestTime.setObjectName("BestTime")
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
        self.scrollDays.setGeometry(QtCore.QRect(480, 280, 241, 291))
        self.scrollDays.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scrollDays.setWidgetResizable(True)
        self.scrollDays.setObjectName("scrollDays")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 239, 289))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollDays.setWidget(self.scrollAreaWidgetContents_2)
        Achievements.setCentralWidget(self.centralwidget)

        self.retranslateUi(Achievements)
        QtCore.QMetaObject.connectSlotsByName(Achievements)

    def retranslateUi(self, Achievements):
        _translate = QtCore.QCoreApplication.translate
        Achievements.setWindowTitle(_translate("Achievements", "MainWindow"))
        self.Achievements_2.setText(_translate("Achievements", "Achievements"))
        self.DaysWithUs.setText(_translate("Achievements", "Your days spent with us"))
        self.BestTime.setText(_translate("Achievements", "Your best time of typing"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Achievements = QtWidgets.QMainWindow()
    ui = Ui_Achievements()
    ui.setupUi(Achievements)
    Achievements.show()
    sys.exit(app.exec())