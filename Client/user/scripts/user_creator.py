from Client.client import signup
from Client.user.scripts.user_updater import *
from db.data_classes import User


def signup_user(username: str, email: str, password: str) -> User:
    def create_password():
        path = Path(users_path.joinpath(Path("Client/user/data/password.json")))
        with open(path, "w") as output_password:
            json.dump({"password": password}, output_password)

    user = {
        "username": username,
        "ids": 0,
        "email": email,
        "disabled": True,
        "registration_date": datetime.utcnow(),
        "achievements": {
            "ids": 0,
            "max_score": 0,
            "avg_accuracy": 0,
            "level": 0,
            "max_speed_accuracy": 0,
            "days_in_row": 0,
            "time_spend": 0,
            "last_visit": datetime.utcnow(),
            "max_symbols_per_day": 0
        }
    }

    user = signup(user_info=User(**user), password=password)

    update_user(user=user)
    create_password()
    return user