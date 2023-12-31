from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QStackedWidget
from PyQt6.QtWidgets import QWidget as QWidget

from Client import SharedData


class RatingWindow(QWidget):
    """
    This class is responsible for the rating window.
    """
    def __init__(self, shared_data: SharedData):
        """
        Initializes the RatingWindow class.

        :param self: The instance of the class that this function belongs to.
        """
        super().__init__()
        self.shared_data = shared_data

    def update_data(self) -> None:
        """
        Updates the data in the main window.

        :return: None
        """
        self.scroll_days.setText(self.shared_data.get_user().username)
        self.scroll_fast.setText(self.shared_data.get_user().username)

    def open_main(self):
        """
        Opens the Main window by setting the current index of the stacked widget to 1.

        :param self: The instance of the class that this function belongs to.
        :return: None
        """

        self.shared_data.update_windows()
        self.stacked_widget.setCurrentIndex(1)

    def setup_ui(self, stacked_widget: QStackedWidget):
        """
        Sets up the user interface for the main window.

        :param self: The instance of the class that this function belongs to.
        :param stacked_widget: QStackedWidget object representing the stacked widget to be used in the main window.
        :return: None
        """
        self.stacked_widget = stacked_widget

        self.setObjectName("MainWindow")
        self.resize(800, 600)
        self.setToolTipDuration(108)
        self.setStyleSheet("background-color: rgb(231, 255, 239);\n"
                           "font: 12pt \"Arial Rounded MT Bold\";")

        self.central_widget = QtWidgets.QWidget(parent=self)
        self.central_widget.setObjectName("centralwidget")

        self.frame = QtWidgets.QFrame(parent=self.central_widget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 181))
        self.frame.setStyleSheet("background-color: rgb(194, 255, 172);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")

        self.rating_lbl = QtWidgets.QLabel(parent=self.frame)
        self.rating_lbl.setGeometry(QtCore.QRect(290, 60, 221, 71))
        self.rating_lbl.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                      "border-radius: 25px;")
        self.rating_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.rating_lbl.setObjectName("RatingLbl")

        self.back_btn = QtWidgets.QPushButton(parent=self.frame)
        self.back_btn.setGeometry(QtCore.QRect(30, 20, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.back_btn.setFont(font)
        self.back_btn.setStyleSheet("""QPushButton:hover{background-color: rgb(235, 255, 197); 
                                                            border: 1px solid black;
                                                            border-radius: 15px;}
                                                         QPushButton:!hover{background-color:
                                                          rgb(235, 255, 197); border-radius: 15px;}
                                                            """)
        self.back_btn.setObjectName("BackBtn")
        self.back_btn.clicked.connect(self.open_main)

        self.scroll_fast = QtWidgets.QTextEdit(parent=self.central_widget)
        self.scroll_fast.setGeometry(QtCore.QRect(100, 280, 241, 291))
        self.scroll_fast.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scroll_fast.setObjectName("scrollFast")

        self.scroll_area_widget_contents = QtWidgets.QWidget()
        self.scroll_area_widget_contents.setGeometry(QtCore.QRect(0, 0, 239, 289))
        self.scroll_area_widget_contents.setObjectName("scrollAreaWidgetContents")

        self.scroll_days = QtWidgets.QTextEdit(parent=self.central_widget)
        self.scroll_days.setGeometry(QtCore.QRect(470, 280, 241, 291))
        self.scroll_days.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scroll_days.setObjectName("scrollDays")

        self.scroll_area_widget_contents_2 = QtWidgets.QWidget()
        self.scroll_area_widget_contents_2.setGeometry(QtCore.QRect(0, 0, 239, 289))
        self.scroll_area_widget_contents_2.setObjectName("scrollAreaWidgetContents_2")

        self.time_lbl = QtWidgets.QLabel(parent=self.central_widget)
        self.time_lbl.setGeometry(QtCore.QRect(70, 200, 301, 71))
        self.time_lbl.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                    "border-radius: 25px;")
        self.time_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.time_lbl.setObjectName("TimeLbl")

        self.accuracy_lbl = QtWidgets.QLabel(parent=self.central_widget)
        self.accuracy_lbl.setGeometry(QtCore.QRect(440, 200, 301, 71))
        self.accuracy_lbl.setStyleSheet("background-color: rgb(235, 255, 197);\n"
                                        "border-radius: 25px;")
        self.accuracy_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.accuracy_lbl.setObjectName("AccuracyLbl")

        stacked_widget.addWidget(self.central_widget)
        self.retranslate_ui()

    def retranslate_ui(self):
        """
        This function sets the translated text for various UI elements in the main window.

        :return: None
        """
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.rating_lbl.setText(_translate("MainWindow", "Rating"))
        self.back_btn.setText(_translate("MainWindow", "Back"))
        self.time_lbl.setText(_translate("MainWindow", "\"The fastest typers\""))
        self.accuracy_lbl.setText(_translate("MainWindow", "The most \"accurate\" typers"))
