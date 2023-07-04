import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget

from Client.user.design.SignUp import SignUpWindow
from Client.user.design.MAIN_WINDOW import MainWindow
from Client.user.design.LogIn import LogInWindow
from Client.user.design.Info import InfoWindow
from Client.user.design.CreateAccount import CreateAccountWindow
from Client.user.design.Account import AccountWindow
from Client.user.design.Achievements import AchievementsWindow
from Client.user.design.Rating import RatingWindow
from Client.user.design.SameUsername import SameUsernameWindow


def setup_windows():
    app = QApplication(sys.argv)

    stacked_widget = QStackedWidget()
    stacked_widget.setFixedSize(800, 600)
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
    create_account_window = CreateAccountWindow(stacked_widget)
    create_account_window.setup_ui()
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

    # 8
    # same_username_window = SameUsernameWindow()
    # same_username_window.setup_ui()
    # stacked_widget.addWidget(same_username_window)

    stacked_widget.setCurrentIndex(0)

    mains_window = QMainWindow()
    mains_window.setCentralWidget(stacked_widget)
    mains_window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    setup_windows()
