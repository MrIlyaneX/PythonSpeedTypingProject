""" Client actions library; all actions for SpeedTypingProject needed for client part located here """

import requests

from DB import *

server_url = "http://127.0.0.1:8000"

user_info = {
    "username": "User11",
    "ids": 0,
    "email": "string@email.com",
    "full_name": "User11",
    "disabled": False,
    "registration_date": "2023-06-17T14:03:19.791028",
    "achievements": {
        "ids": 0,
        "max_score": 0,
        "avg_accuracy": 0,
        "level": 0,
        "max_speed_accuracy": 0,
        "days_in_row": 0,
        "time_spend": 0,
        "last_visit": "2023-06-17T14:04:12.127Z",
        "max_symbols_per_day": 0
    }
}

user_model = User(**user_info)


def signup(password: str = "secret"):
    url = f"{server_url}/signup"
    response = requests.post(url, json=user_info, params={"password": password})
    if response.status_code != 200:
        print("Error:", response.status_code)
        print(response.text)
        exit(19)
    return response.json()


def login(username: str, password: str):
    url = f"{server_url}/token"
    payload = {
        "username": username,
        "password": password
    }
    response = requests.post(url, data=payload)
    if response.status_code != 200:
        print("Error:", response.status_code)
        print(response.text)
        exit(20)
    return response.json()["access_token"]


def get_info(header):
    url = f"{server_url}/users/me/"

    response = requests.get(url, headers=header)
    if response.status_code != 200:
        print("Error:", response.status_code)
        print(response.text)
        exit(21)

    return response.json()


def upload_info(user: User, header):
    url = f"{server_url}/users/me/upload"
    user.registration_date = user.registration_date.isoformat()
    user.achievements.last_visit = user.achievements.last_visit.isoformat()
    response = requests.post(url, headers=header, json=user.dict())
    if response.status_code != 200:
        print("Error:", response.status_code)
        print(response.text)
        exit(22)

    return response.json()


if __name__ == "__main__":
    cur_user = signup()
    access_token = login(user_model.username, password="secret")
    headers = {
        "Authorization": "Bearer " + access_token
    }
    ans = get_info(headers)
    print(ans)

    user_model.email = "new@mail.com"
    ans1 = upload_info(user_model, headers)
    print(ans1)

# {"detail":[
# {"loc":["body","username"],
# "msg":"field required",
# "type":"value_error.missing"},

# {"loc":["body","password"],
# "msg":"field required",
# "type":"value_error.missing"}
# ]}
