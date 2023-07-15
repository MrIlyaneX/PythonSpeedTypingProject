import datetime

from PyQt6.QtWidgets import QStackedWidget
from Client.client_runner import get_user, upload_user_info
from Client.models.data_classes import User, Stats


class SharedData:
    """
    A class that stores the data that is shared between all the windows.
    Uses Singleton design pattern.

    :param widget: The stacked widget that contains all the windows.
    """

    def __init__(self, widget: QStackedWidget):
        self.stacked_widget = widget
        self.header: dict | None = None
        self.user: User | None = None
        self.windows = []

    def add_window(self, window) -> None:
        """
        Adds a window to the list of windows.

        :param window: The window to add.
        :return: None
        """

        self.windows.append(window)

    def get_user(self) -> User:
        """
        Gets the user.
        If the token is None, it returns a disabled user with default values.
        If the token is not None, it returns the user from the server.

        :return: The user.
        """

        if self.header is None:
            user: dict = {
                "username": "",
                "email": "",
                "disabled": True,
                "achievements": {
                    "max_score": 0,
                    "avg_accuracy": 0,
                    "max_speed_accuracy": 0,
                    "last_visit": datetime.datetime.utcnow().isoformat(),
                    "max_symbols_per_day": 0,
                }
            }
            self.user = User(**user)
        else:
            self.user = get_user(header=self.header)
        return self.user

    def get_stats(self) -> Stats:
        """
        Gets the stats of the user.

        :return: The stats of the user.
        """

        return self.get_user().achievements

    def update_accuracy(self, accuracy) -> None:
        """
        Updates the accuracy of the user.

        :param accuracy: The accuracy of the user.
        :return: None
        """

        if self.user is not None:
            self.user.achievements.avg_accuracy = accuracy

    def update_score(self, score) -> None:
        """
        Updates the score of the user.

        :param score: The score of the user.
        :return: None
        """

        if self.user is not None:
            self.user.achievements.max_score = score

    def upload_info_on_server(self) -> None:
        """
        Uploads the user info on the server.

        :return: None
        """

        if self.header is not None and self.user is not None:
            if not self.user.disabled:
                upload_user_info(self.header, self.user)
                user = self.get_user()
                if isinstance(user, User):
                    self.user = user

    def update_windows(self) -> None:
        """
        Updates the data to display in all the windows.

        :return: None
        """

        # 5: Account
        # 6: Achievements
        # 7: Rating
        for i in self.windows:
            i.update_data()

    def get_days(self) -> str:
        return '0'
