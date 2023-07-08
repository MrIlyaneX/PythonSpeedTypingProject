from db.data_classes import User


class SharedData:
    def __init__(self):
        self.header: dict | None = None
        self.user: User | None = None
