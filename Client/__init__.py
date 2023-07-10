from Client.models.data_classes import User


class SharedData:
    def __init__(self):
        self.header: dict | None = None
        self.user: User | None = None

    def get_user(self) -> User | str:
        if self.user is None:
            return User()
        return self.user
