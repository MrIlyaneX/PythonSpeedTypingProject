from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QStackedWidget
from PyQt6.QtWidgets import QWidget as QWidget


class AccountWindow(QWidget):
    def open_main(self):
        self.stacked_widget.setCurrentIndex(1)

    def setup_ui(self, stacked_widget: QStackedWidget):
        self.stacked_widget = stacked_widget

        Account = QtWidgets.QMainWindow()
        Account.setObjectName("Account")
        Account.resize(800, 600)
        Account.setStyleSheet("background-color: rgb(231, 255, 239);\n"
                              "font: 12pt \"Arial Rounded MT Bold\";")

        self.central_widget = QtWidgets.QWidget(parent=Account)
        self.central_widget.setObjectName("centralwidget")

        self.frame = QtWidgets.QFrame(parent=self.central_widget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 181))
        self.frame.setStyleSheet(" background-color: rgb(194, 255, 172);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")

        self.account_lbl = QtWidgets.QLabel(parent=self.frame)
        self.account_lbl.setGeometry(QtCore.QRect(300, 50, 221, 81))
        self.account_lbl.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                      "border-radius: 25px;")
        self.account_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.account_lbl.setObjectName("AccountLbl")

        self.username_txt = QtWidgets.QTextBrowser(parent=self.central_widget)
        self.username_txt.setGeometry(QtCore.QRect(60, 290, 301, 61))
        self.username_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.username_txt.setObjectName("UsernameTxt")

        self.days_txt = QtWidgets.QTextBrowser(parent=self.central_widget)
        self.days_txt.setGeometry(QtCore.QRect(80, 500, 81, 51))
        self.days_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.days_txt.setObjectName("DaysTxt")

        self.time_txt = QtWidgets.QTextBrowser(parent=self.central_widget)
        self.time_txt.setGeometry(QtCore.QRect(530, 370, 171, 61))
        self.time_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.time_txt.setObjectName("TimeTxt")

        self.back_btn = QtWidgets.QPushButton(parent=self.frame)
        self.back_btn.setGeometry(QtCore.QRect(30, 20, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.back_btn.setFont(font)
        self.back_btn.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                    "border-radius: 15px;")
        self.back_btn.setObjectName("BackBtn")

        # Button action to come back to the MainWindow
        self.back_btn.clicked.connect(self.open_main)

        self.username_lbl = QtWidgets.QLabel(parent=self.central_widget)
        self.username_lbl.setGeometry(QtCore.QRect(40, 220, 331, 61))
        self.username_lbl.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                       "border-radius: 25px;")
        self.username_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.username_lbl.setObjectName("UsernameLbl")

        self.time_lbl = QtWidgets.QLabel(parent=self.central_widget)
        self.time_lbl.setGeometry(QtCore.QRect(500, 300, 221, 61))
        self.time_lbl.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                   "border-radius: 25px;")
        self.time_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.time_lbl.setObjectName("TimeLbl")

        self.days_lbl = QtWidgets.QLabel(parent=self.central_widget)
        self.days_lbl.setGeometry(QtCore.QRect(170, 500, 121, 61))
        self.days_lbl.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                   "border-radius: 25px;")
        self.days_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.days_lbl.setObjectName("DaysLbl")

        self.with_us_lbl = QtWidgets.QLabel(parent=self.central_widget)
        self.with_us_lbl.setGeometry(QtCore.QRect(40, 430, 271, 61))
        self.with_us_lbl.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                     "border-radius: 25px;")
        self.with_us_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.with_us_lbl.setObjectName("WithUsLbl")

        Account.setCentralWidget(self.central_widget)

        # Button action to come back to the MainWindow
        self.back_btn.clicked.connect(self.open_main)

        stacked_widget.addWidget(self.central_widget)
        self.retranslate_ui(self)

    def retranslate_ui(self, Account):
        _translate = QtCore.QCoreApplication.translate
        Account.setWindowTitle(_translate("Account", "MainWindow"))
        self.account_lbl.setText(_translate("Account", "Account"))
        self.back_btn.setText(_translate("Account", "Back"))
        self.username_lbl.setText(_translate("Account", "Username"))
        self.time_lbl.setText(_translate("Account", "Your best time"))
        self.days_lbl.setText(_translate("Account", "days"))
        self.with_us_lbl.setText(_translate("Account", "You are with us already"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    stacked_widget = QStackedWidget()
    stacked_widget.setFixedSize(800, 600)

    account_window = AccountWindow()
    account_window.setup_ui(stacked_widget)

    main_window = QtWidgets.QMainWindow()
    main_window.setCentralWidget(stacked_widget)
    main_window.show()

    sys.exit(app.exec())
