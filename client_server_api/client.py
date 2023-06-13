import requests

from DB import *

server_url = "http://127.0.0.1:8000"


def post_user_info(info: UserInfo, link: int):
    url = f"{server_url}/user/{link}"
    response = requests.post(url, json=info.dict())
    return response.json()


def get_user_info(link: int):
    url = f"{server_url}/user/{link}"
    response = requests.get(url)
    return response.json()
