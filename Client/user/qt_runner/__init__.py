import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget

from PyQt6 import QtCore, QtGui, QtWidgets

from Client.user.design.SignUp import SignUpWindow
from Client.user.design.MainWindow import MainWindow
from Client.user.design.LogIn import LogInWindow
from Client.user.design.Info import InfoWindow
from Client.user.design.CreateAccount import CreateAccountWindow
from Client.user.design.Account import AccountWindow
from Client.user.design.Achievements import AchievementsWindow
from Client.user.design.Rating import RatingWindow


def setup_windows():
    app = QApplication(sys.argv)

    stacked_widget = QStackedWidget()
    stacked_widget.setFixedSize(800, 600)
    stacked_widget.setStyleSheet("background-color: rgb(231, 255, 239);\n"
                                 "font: 12pt \"Arial Rounded MT Bold\";")

    stacked_widget.show()

    # 0
    signup_window = SignUpWindow()
    signup_window.setup_ui(stacked_widget)
    stacked_widget.addWidget(signup_window.central_widget)

    # 1
    main_window = MainWindow()
    main_window.setup_ui(stacked_widget)
    stacked_widget.addWidget(main_window.central_widget)

    # 2
    login_window = LogInWindow()
    login_window.setup_ui(stacked_widget)
    stacked_widget.addWidget(login_window.central_widget)

    # 3
    info_window = InfoWindow()
    info_window.setup_ui(stacked_widget)
    stacked_widget.addWidget(info_window.info)

    # 4
    create_account_window = CreateAccountWindow()
    create_account_window.setup_ui(stacked_widget)
    stacked_widget.addWidget(create_account_window.central_widget)

    # 5
    account_window = AccountWindow()
    account_window.setup_ui(stacked_widget)
    stacked_widget.addWidget(account_window.central_widget)

    # 6
    achievements_window = AchievementsWindow()
    achievements_window.setup_ui(stacked_widget)
    stacked_widget.addWidget(achievements_window.central_widget)

    # 7
    rating_window = RatingWindow()
    rating_window.setup_ui(stacked_widget)
    stacked_widget.addWidget(rating_window.central_widget)


    stacked_widget.setCurrentIndex(0)
    stacked_widget.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    setup_windows()
