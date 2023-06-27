""" Client actions library; all actions for SpeedTypingProject needed for client part located here """
import json

import requests

from db.data_classes import *

server_url = "http://127.0.0.1:8000"


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


def signup(username: str, user_email: str, password: str) -> User:
    """
    Creates user on the server

    :param username: username
    :param user_email: user email 
    :param password: user password
    :return: User
    """

    url = f"{server_url}/signup"
    user_dict = {"username": username, "email": user_email}
    response = requests.post(url, json=user_dict, params={
                             "password": password})
    if response.status_code != 200:
        print("Error:", response.status_code)
        print(response.text)
        exit(19)
    return User(**response.json())


def login(username: str, password: str) -> str:
    """
    Gets token for future authentication related actions

    :param username: username
    :param password: password
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
        exit(20)
    return response.json()["access_token"]


def get_info(header) -> User:
    """
    Gets info from the server about user

    :param header: header with token
    :return: user info in User format
    """
    url = f"{server_url}/users/me/"

    response = requests.get(url, headers=header)
    if response.status_code != 200:
        print("Error:", response.status_code)
        print(response.text)
        exit(21)

    return User(**response.json())


def upload_info(user_info: User, header) -> User:
    """
    For now uploads achievements data in User at the server side

    :param user_info: user info in User format to upload
    :param header: header with token
    :return: user info in User format
    """
    url = f"{server_url}/users/me/upload"
    user_dict = user_to_dict(user_info)
    response = requests.post(url, headers=header, json=user_dict)
    if response.status_code == 401:
        print("Error:", response.status_code)
        print(response.text)
        print("Authorization error")
        exit(23)
    if response.status_code != 200:
        print("Error:", response.status_code)
        print(response.text)
        exit(22)

    return User(**response.json())


def get_file(language: str, header) -> None:
    """
    Gets file with chosen language from the server to user/data/file_name

    :param language: language of the file in type "en" or "ru"
    :param header: header with token
    :return: None
    """

    url = f"{server_url}/files/words/{language}"
    response = requests.get(url, headers=header)

    if response.status_code == 401:
        print("Error:", response.status_code)
        print(response.text)
        print("Authorization error")
        exit(23)
    if response.status_code != 200:
        print("Error:", response.status_code)
        print(response.text)
        exit(24)

    content_disposition = response.headers.get("content-disposition")
    filename = content_disposition.split("filename=")[-1].strip('\"')
    save_path = f"user/data/words/{filename}"
    with open(save_path, "w") as file:
        json.dump(response.json(), file)
