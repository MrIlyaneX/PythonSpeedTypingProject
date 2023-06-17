""" Client actions library; all actions for SpeedTypingProject needed for client part located here """

import requests
from DB import *

server_url = "http://127.0.0.1:8000"


def get_token(name: str, password: SecretStr):
    """ Requests token from the server """
    url = f"{server_url}/user/login"
    response = requests.post(url, data={"username": name, "password": password.get_secret_value()})
    response.raise_for_status()
    return response.json()["access_token"]


def signup(user: UserInfo):
    """ Sign Up user into the server """
    url = f"{server_url}/user/signup"
    user.password = user.password.get_secret_value()
    user.registration_date = user.registration_date.isoformat()
    response = requests.post(url, json=user.dict())
    if response.status_code != 200:
        print(f"Signup failed with status code: {response.status_code}")
        print(f"Response content: {response.content}")
        return response.status_code

    access_token = get_token(user.name, SecretStr(user.password))
    return access_token


def post_user_info(info: UserInfo, link: int, token: str):
    """ Uploads information about the user to the web API (server) """
    url = f"{server_url}/user/{link}"
    info.password = info.password.get_secret_value()
    info_dict = info.dict()
    info_dict['registration_date'] = info_dict['registration_date'].isoformat()
    response = requests.post(url, json=info_dict, headers={"Authorization": f"Bearer {token}"})
    return response.json()


def get_user_info(link: int, token: str):
    """ Gets information about the user from the web API (server) """
    url = f"{server_url}/user/{link}"
    response = requests.get(url, headers={"Authorization": f"Bearer {token}"})
    response.raise_for_status()
    return response.json()
