import datetime

from Client.models.data_classes import User, Stats
from Client.client_runner import get_user, upload_user_info


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
        return self.get_user().achievements

    def update_accuracy(self, accuracy):
        if self.user is not None:
            self.user.achievements.avg_accuracy = accuracy

    def update_score(self, score):
        if self.user is not None:
            self.user.achievements.max_score = score

    def upload_info_on_server(self):
        if self.header is not None and self.user is not None:
            if not self.user.disabled:
                upload_user_info(self.header, self.user)
