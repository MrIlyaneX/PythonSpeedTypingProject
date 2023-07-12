import datetime

from Client.models.data_classes import User, Stats
from Client.client_runner import get_user


class SharedData:
    def __init__(self):
        self.header: dict | None = None
        self.user: User | None = None

    def get_user(self) -> User:
        if self.header is None:
            user: dict = {
                "username": "",
                "email": "",
                "disabled": True,
                "hashed_password": "",
                "achievements": {
                    "max_score": 0,
                    "avg_accuracy": 0,
                    "max_speed_accuracy": 0,
                    "last_visit": datetime.datetime.utcnow(),
                }
            }
            self.user = User(**user)
        else:
            self.user = get_user(header=self.header)
        return self.user

    def get_stats(self) -> Stats:
        return self.get_user().achievements
