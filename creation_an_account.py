# Form implementation generated from reading ui file 'creation_an_account.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_CreateAccWindow(object):
    def setupUi(self, CreateAccWindow):
        CreateAccWindow.setObjectName("CreateAccWindow")
        CreateAccWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        CreateAccWindow.setFont(font)
        CreateAccWindow.setStyleSheet("background-color: rgb(231, 255, 239);\n"
"") 
        CreateAccWindow.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.centralwidget = QtWidgets.QWidget(parent=CreateAccWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Createaccount = QtWidgets.QLabel(parent=self.centralwidget)
        self.Createaccount.setGeometry(QtCore.QRect(0, 0, 801, 181))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Createaccount.sizePolicy().hasHeightForWidth())
        self.Createaccount.setSizePolicy(sizePolicy)
        self.Createaccount.setMinimumSize(QtCore.QSize(0, 181))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.Createaccount.setFont(font)
        self.Createaccount.setAcceptDrops(False)
        self.Createaccount.setToolTipDuration(-1)
        self.Createaccount.setStyleSheet(" background-color: rgb(194, 255, 172);\n"
"")
        self.Createaccount.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.Createaccount.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.Createaccount.setScaledContents(False)
        self.Createaccount.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Createaccount.setWordWrap(False)
        self.Createaccount.setIndent(-1)
        self.Createaccount.setObjectName("Createaccount")
        self.Write_your_name = QtWidgets.QLabel(parent=self.centralwidget)
        self.Write_your_name.setGeometry(QtCore.QRect(290, 200, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.Write_your_name.setFont(font)
        self.Write_your_name.setStyleSheet("background-color: rgb(235, 255, 197);\n"
"border-radius: 25px;")
        self.Write_your_name.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.Write_your_name.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Write_your_name.setObjectName("Write_your_name")
        self.Create_a_password = QtWidgets.QLabel(parent=self.centralwidget)
        self.Create_a_password.setGeometry(QtCore.QRect(290, 360, 201, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Create_a_password.sizePolicy().hasHeightForWidth())
        self.Create_a_password.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.Create_a_password.setFont(font)
        self.Create_a_password.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.Create_a_password.setStyleSheet("background-color: rgb(235, 255, 197);\n"
"border-radius: 25px;")
        self.Create_a_password.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Create_a_password.setObjectName("Create_a_password")
        self.NameText = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.NameText.setGeometry(QtCore.QRect(300, 290, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.NameText.setFont(font)
        self.NameText.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.NameText.setObjectName("NameText")
        self.Passwordtext = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Passwordtext.setGeometry(QtCore.QRect(300, 450, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.Passwordtext.setFont(font)
        self.Passwordtext.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Passwordtext.setObjectName("Passwordtext")
        self.Save = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Save.setGeometry(QtCore.QRect(640, 530, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.Save.setFont(font)
        self.Save.setStyleSheet("background-color: rgb(235, 255, 197);\n"
"border-radius: 25px;")
        self.Save.setObjectName("Save")
        CreateAccWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(CreateAccWindow)
        QtCore.QMetaObject.connectSlotsByName(CreateAccWindow)

    def retranslateUi(self, CreateAccWindow):
        _translate = QtCore.QCoreApplication.translate
        CreateAccWindow.setWindowTitle(_translate("CreateAccWindow", "CreateAccWindow"))
        CreateAccWindow.setToolTip(_translate("CreateAccWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.Createaccount.setText(_translate("CreateAccWindow", "Create an account"))
        self.Write_your_name.setText(_translate("CreateAccWindow", "Write you name"))
        self.Create_a_password.setText(_translate("CreateAccWindow", "Create a password"))
        self.Save.setText(_translate("CreateAccWindow", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CreateAccWindow = QtWidgets.QCreateAccWindow()
    ui = Ui_CreateAccWindow()
    ui.setupUi(CreateAccWindow)
    CreateAccWindow.show()
    sys.exit(app.exec())
