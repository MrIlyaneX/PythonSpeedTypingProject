""" Client actions library; all actions for SpeedTypingProject needed for client part located here """
import json

import requests

from db.data_classes import *


def user_to_dict(user: User) -> dict:
    """
    Converts User to dict

    :param user: user data of type User
    :return: dict with user data in json format
    """

    user_copy = user.copy()

    if isinstance(user_copy.achievements.last_visit, datetime):
        user_copy.achievements.last_visit = user_copy.achievements.last_visit.isoformat()

    user_copy.achievements = user_copy.achievements.dict()
    user_copy = user_copy.dict()
    return user_copy


def signup(username: str,
           user_email: str,
           password: str,
           server_url: str = "http://127.0.0.1:8000"
           ) -> User | dict:
    """
    Creates user on the server

    :param username: username
    :param user_email: user email 
    :param password: user password
    :param server_url: url of the server
    :return: User
    """

    url = f"{server_url}/signup"
    response = requests.post(url, params={"password": password, "username": username, "user_email": user_email})
    if response.status_code != 200:
        print("Error:", response.status_code)
        print(response.text)
        print(1000)
        return {"msg": "Invalid Sign Up", "code": 20}
    return User(**response.json())


def login(
        username: str,
        password: str,
        server_url: str = "http://127.0.0.1:8000"
) -> Token | dict:
    """
    Gets token for future authentication related actions

    :param username: username
    :param password: password
    :param server_url: url of the server
    :return: token
    """
    url = f"{server_url}/token"
    payload = {
        "username": username,
        "password": password
    }
    response = requests.post(url, data=payload)
    if response.status_code != 200:
        print("Error:", response.status_code)
        print(response.text)
        return {"msg": "Invalid Log In", "code": 20}
    return response.json()


def get_info(
        header,
        server_url: str = "http://127.0.0.1:8000"
) -> User | dict:
    """
    Gets info from the server about user

    :param header: header with token
    :param server_url: url of the server
    :return: user info in User format
    """
    url = f"{server_url}/users/me/"

    response = requests.get(url, headers=header)
    if response.status_code != 200:
        print("Error:", response.status_code)
        print(response.text)
        return {"msg": " Failed to get information from server", "code": 21}

    return User(**response.json())


def upload_info(
        user_info: User,
        header: dict,
        server_url: str = "http://127.0.0.1:8000"
) -> User | dict:
    """
    For now uploads achievements data in User at the server side

    :param user_info: user info in User format to upload
    :param header: header with token
    :param server_url: url of the server
    :return: user info in User format
    """
    url = f"{server_url}/users/me/upload"
    user_dict = user_to_dict(user_info)
    response = requests.post(url, headers=header, json=user_dict)
    if response.status_code == 401:
        print("Error:", response.status_code)
        print(response.text)
        print("Authorization error")
        return {"msg": "Authorization error during uploading info", "code": 23}
    if response.status_code != 200:
        print("Error:", response.status_code)
        print(response.text)
        return {"msg": " Failed to upload info to the server", "code": 22}

    return User(**response.json())


def get_file(
        language: str,
        header,
        server_url: str = "http://127.0.0.1:8000"
) -> None | dict:
    """
    Gets file with chosen language from the server to user/data/file_name

    :param language: language of the file in type "en" or "ru"
    :param header: header with token
    :param server_url: url of the server
    :return: None
    """

    url = f"{server_url}/files/words/{language}"
    response = requests.get(url, headers=header)

    if response.status_code == 401:
        print("Error:", response.status_code)
        print(response.text)
        print("Authorization error")
        return {"msg": "Authorization error during uploading info", "code": 23}
    if response.status_code != 200:
        print("Error:", response.status_code)
        print(response.text)
        return {"msg": "Failed to get words from chosen language from the server", "code": 24}

    content_disposition = response.headers.get("content-disposition")
    filename = content_disposition.split("filename=")[-1].strip('\"')
    save_path = f"user/data/words/{filename}"
    with open(save_path, "w") as file:
        json.dump(response.json(), file)


def get_leaderboard(server_url: str = "http://127.0.0.1:8000") -> dict:
    """
    :param server_url: url of the server
    """
    url = f"{server_url}/leaderboard"
    response = requests.get(url)

    if response.status_code != 200:
        print("Error:", response.status_code)
        print(response.text)
        return {"msg": "Failed to get leaderboard from the server", "code": 25}

    return response.json()
