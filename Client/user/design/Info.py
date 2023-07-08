from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QStackedWidget

from Client import SharedData


class InfoWindow(object):
    def __init__(self, shared_data: SharedData):
        super().__init__()
        self.shared_data = shared_data

    def open_main(self):
        """
        Opens the Main window by setting the current index of the stacked widget to 1.

        :param self: The instance of the class that this method belongs to.
        :return: None
        """
        self.stacked_widget.setCurrentIndex(1)

    def setup_ui(self, stacked_widget: QStackedWidget):
        """
        Sets up the user interface for the main window.

        :param self: The instance of the class that this function belongs to.
        :return: None
        """
        self.stacked_widget = stacked_widget

        self.info = QtWidgets.QWidget()
        self.info.setObjectName("info")
        self.info.setStyleSheet("background-color: rgb(231, 255, 239);\n"
                                "font: 12pt \"Arial Rounded MT Bold\";")

        self.frame = QtWidgets.QFrame(self.info)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 181))
        self.frame.setStyleSheet(" background-color: rgb(194, 255, 172);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")

        self.info_lbl = QtWidgets.QLabel(self.info)
        self.info_lbl.setGeometry(QtCore.QRect(300, 60, 201, 71))
        self.info_lbl.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                    "border-radius: 25px;")
        self.info_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.info_lbl.setObjectName("info_lbl")
        self.back_btn = QtWidgets.QPushButton(parent=self.frame)
        self.back_btn.setGeometry(QtCore.QRect(30, 20, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.back_btn.setFont(font)
        self.back_btn.setStyleSheet("""QPushButton:hover{background-color: rgb(235, 255, 197); 
                                    border: 1px solid black;border-radius: 25px;}
                                    QPushButton:!hover{background-color: rgb(235, 255, 197);
                                    border-radius: 25px;}""")
        self.back_btn.setObjectName("BackBtn")

        # Button action to come back to the MainWindow
        self.back_btn.clicked.connect(self.open_main)

        self.description_text = QtWidgets.QLabel(self.info)
        self.description_text.setGeometry(QtCore.QRect(60, 230, 671, 241))
        self.description_text.setFont(QtGui.QFont("Arial Rounded MT Bold", 12))
        self.description_text.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                            "border-radius: 25px;\n"
                                            "\n"
                                            "\n"
                                            "")
        self.description_text.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.description_text.setWordWrap(True)
        self.description_text.setObjectName("description_text")

        self.retranslate_ui(self.info)
        QtCore.QMetaObject.connectSlotsByName(self.info)

        stacked_widget.addWidget(self.info)

    def retranslate_ui(self, info):
        """
        This function sets the translated text for various UI elements in the main window.

        :return: None
        """
        _translate = QtCore.QCoreApplication.translate
        info.setWindowTitle(_translate("Info", "MainWindow"))
        self.info_lbl.setText(_translate("Info", "Information"))
        self.back_btn.setText(_translate("Info", "Back"))
        self.description_text.setText(_translate("Info",
                                                 "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;"
                                                 "color:#262626;\">Our typing speed application project is designed for"
                                                 " entertainment purposes, without a strong scientific focus. While"
                                                 " similar resources already exist on the Internet, they are often"
                                                 " imperfect, with users complaining about limited functionality,"
                                                 " excessive advertising, a complex interface, and inflexible settings."
                                                 "</span></p></body></html>"))
