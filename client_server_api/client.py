import requests
from DB import *

server_url = "http://127.0.0.1:8000"


def post_user_info(info: UserInfo, link: int):
    url = f"{server_url}/user/{link}"
    info_dict = info.dict()
    info_dict['registration_date'] = info_dict['registration_date'].isoformat()
    info_dict['last_visit'] = info_dict['last_visit'].isoformat()
    response = requests.post(url, json=info_dict)
    return response.json()


def get_user_info(link: int):
    url = f"{server_url}/user/{link}"
    response = requests.get(url)
    return response.json()
