import sys

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QStackedWidget

from Client import SharedData
from Client.user.design.Account import AccountWindow
from Client.user.design.Achievements import AchievementsWindow
from Client.user.design.CreateAccount import CreateAccountWindow
from Client.user.design.Info import InfoWindow
from Client.user.design.LogIn import LogInWindow
from Client.user.design.MainWindow import MainWindow
from Client.user.design.Rating import RatingWindow
from Client.user.design.SignUp import SignUpWindow


def setup_windows():
    """
    Sets up all windows and adds them to the stacked widget.

    shared_data is passed to all windows. Singleton pattern.
    stacked_widget is passed to all windows for window switching.

    :return: None
    """

    app = QApplication(sys.argv)
    stacked_widget = QStackedWidget()
    shared_data = SharedData(stacked_widget)

    stacked_widget.setFixedSize(800, 600)
    stacked_widget.setStyleSheet("background-color: rgb(231, 255, 239);\n"
                                 "font: 12pt \"Arial Rounded MT Bold\";")
    stacked_widget.setWindowIcon(QIcon(r"Client\user\data\icon.jpg"))
    stacked_widget.show()

    # 0
    signup_window = SignUpWindow(shared_data)
    signup_window.setup_ui(stacked_widget)
    stacked_widget.addWidget(signup_window.central_widget)

    # 1
    main_window = MainWindow(shared_data)
    main_window.setup_ui(stacked_widget)
    main_window.display_text("Try your speed typing...")
    stacked_widget.addWidget(main_window.central_widget)

    # 2
    login_window = LogInWindow(shared_data)
    login_window.setup_ui(stacked_widget)
    stacked_widget.addWidget(login_window.central_widget)

    # 3
    info_window = InfoWindow(shared_data)
    info_window.setup_ui(stacked_widget)
    stacked_widget.addWidget(info_window.info)

    # 4
    create_account_window = CreateAccountWindow(shared_data)
    create_account_window.setup_ui(stacked_widget)
    stacked_widget.addWidget(create_account_window.central_widget)

    # 5 needs updating
    account_window = AccountWindow(shared_data)
    account_window.setup_ui(stacked_widget)
    stacked_widget.addWidget(account_window.central_widget)

    # 6 needs updating
    achievements_window = AchievementsWindow(shared_data)
    achievements_window.setup_ui(stacked_widget)
    stacked_widget.addWidget(achievements_window.central_widget)

    # 7 needs updating
    rating_window = RatingWindow(shared_data)
    rating_window.setup_ui(stacked_widget)
    stacked_widget.addWidget(rating_window.central_widget)

    shared_data.add_window(account_window)
    shared_data.add_window(achievements_window)
    shared_data.add_window(rating_window)

    stacked_widget.setCurrentIndex(0)
    stacked_widget.show()

    sys.exit(app.exec())
