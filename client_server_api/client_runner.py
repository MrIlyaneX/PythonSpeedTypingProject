import time
from datetime import datetime
from getpass import getpass

import requests

from client import *
from DB import *

server_url = "http://127.0.0.1:8000"

user_info = {
    "username": "qw",
    "ids": 0,
    "email": "string@email.com",
    "full_name": "qw",
    "disabled": False,
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

user_model = User(**user_info)

if __name__ == "__main__":
    # print(user_to_dict(user_model))

    start = time.time()
    signup(user_info=user_model, password="secret")
    end = time.time()
    print("signup", format(end - start, ".20f"))

    start = time.time()
    access_token = login(user_model.username, password="secret")
    end = time.time()
    print("login", format(end - start, ".20f"))
    headers = {
        "Authorization": "Bearer " + access_token
    }

    start = time.time()
    ans = get_info(headers)
    # print(ans, headers)
    end = time.time()
    print("get_info", format(end - start, ".20f"))

    user_model.achievements.level = 100

    start = time.time()
    ans1 = upload_info(user_model, headers)
    end = time.time()
    print("upload", format(end - start, ".20f"))
    # print(ans1)
