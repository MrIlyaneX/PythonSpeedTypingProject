from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QStackedWidget
from PyQt6.QtWidgets import QWidget

from Client import SharedData


class AchievementsWindow(QWidget):
    def __init__(self, shared_data: SharedData):
        super().__init__()
        self.shared_data = shared_data

    def open_main(self):
        """
        Opens the Main window by setting the current index of the stacked widget to 1.

        :param self: The instance of the class that this function belongs to.
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

        Achievements = QtWidgets.QMainWindow()
        Achievements.setObjectName("Achievements")
        Achievements.resize(800, 600)
        Achievements.setStyleSheet("background-color: rgb(231, 255, 239);\n"
                                   "font: 12pt \"Arial Rounded MT Bold\";\n"
                                   "")

        self.central_widget = QtWidgets.QWidget(parent=Achievements)
        self.central_widget.setObjectName("centralwidget")

        self.frame = QtWidgets.QFrame(parent=self.central_widget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 800, 181))
        self.frame.setStyleSheet(" background-color: rgb(194, 255, 172);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")

        self.back_btn = QtWidgets.QPushButton(parent=self.frame)
        self.back_btn.setGeometry(QtCore.QRect(30, 20, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.back_btn.setFont(font)
        self.back_btn.setStyleSheet("""QPushButton:hover{background-color: rgb(235, 255, 197); 
                                                                    border: 1px solid black;
                                                                    border-radius: 25px;}
                                                                 QPushButton:!hover{background-color: rgb(235, 255, 197);
                                                                  border-radius: 25px;}
                                                                    """)
        self.back_btn.setObjectName("back_btn")

        self.back_btn.clicked.connect(self.open_main)

        self.achievements_lbl = QtWidgets.QLabel(parent=self.frame)
        self.achievements_lbl.setGeometry(QtCore.QRect(290, 40, 221, 81))
        self.achievements_lbl.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                            "border-radius: 25px;")
        self.achievements_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.achievements_lbl.setObjectName("achievements_lbl")

        self.scroll_time = QtWidgets.QScrollArea(parent=self.central_widget)
        self.scroll_time.setGeometry(QtCore.QRect(100, 280, 241, 291))
        self.scroll_time.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scroll_time.setWidgetResizable(True)
        self.scroll_time.setObjectName("scroll_time")

        self.scroll_area_widget_contents = QtWidgets.QWidget()
        self.scroll_area_widget_contents.setGeometry(QtCore.QRect(0, 0, 239, 289))
        self.scroll_area_widget_contents.setObjectName("scrollAreaWidgetContents")

        self.scroll_time.setWidget(self.scroll_area_widget_contents)

        self.scroll_days = QtWidgets.QScrollArea(parent=self.central_widget)
        self.scroll_days.setGeometry(QtCore.QRect(470, 280, 241, 291))
        self.scroll_days.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scroll_days.setWidgetResizable(True)
        self.scroll_days.setObjectName("scrollDays")

        self.scroll_area_widget_contents_2 = QtWidgets.QWidget()
        self.scroll_area_widget_contents_2.setGeometry(QtCore.QRect(0, 0, 239, 289))
        self.scroll_area_widget_contents_2.setObjectName("scrollAreaWidgetContents_2")

        self.scroll_days.setWidget(self.scroll_area_widget_contents_2)

        self.best_time_lbl = QtWidgets.QLabel(parent=self.central_widget)
        self.best_time_lbl.setGeometry(QtCore.QRect(70, 200, 301, 71))
        self.best_time_lbl.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                         "border-radius: 25px;")
        self.best_time_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.best_time_lbl.setObjectName("BestTimeLbl")

        self.days_with_us_labl = QtWidgets.QLabel(parent=self.central_widget)
        self.days_with_us_labl.setGeometry(QtCore.QRect(440, 200, 301, 71))
        self.days_with_us_labl.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                             "border-radius: 25px;")
        self.days_with_us_labl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.days_with_us_labl.setObjectName("DaysWithUsLabl")

        Achievements.setCentralWidget(self.central_widget)

        stacked_widget.addWidget(self.central_widget)
        self.retranslate_ui()

    def retranslate_ui(self):
        """
        This function sets the translated text for various UI elements in the main window.

        :return: None
        """
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Achievements", "MainWindow"))
        self.back_btn.setText(_translate("Achievements", "Back"))
        self.achievements_lbl.setText(_translate("Achievements", "Achievements"))
        self.best_time_lbl.setText(_translate("Achievements", "Your best time of typing"))
        self.days_with_us_labl.setText(_translate("Achievements", "Your days spent with us"))
