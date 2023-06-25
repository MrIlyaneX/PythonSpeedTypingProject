""" Works with client data exchange to server and inner data """
import random

from Client.user.scripts.user_updater import *
from Client.user.scripts.user_creator import *
from db.data_classes import User, Token

server_url = "http://127.0.0.1:8000"


def get_data():
    """
    Temporary function for emulating user signup.
    Returns data for successful signup.


    :return: {"username": "value", "email": "value@email.com", "password": "value"}
    """

    return {"username": "qweq", "email": "q@email.com", "password": "qe"}


def data_from_login() -> dict:
    """
    Emulates user login actions

    :return: {"username": "value", "password": "value"}
    """
    return {"username": str(random.seed), "password": "q"}


def runner_main(to_signup: bool = True, to_remember: bool = True):
    """
    Function for user work with server

    :param to_remember:
    :param to_signup:
    :return:
    """

    user: User
    token: Token
    if to_signup:
        user = signup_user(**get_data())
        token = login(user.username, get_data()["password"])
    if not to_signup and to_remember:
        user, password = get_user(), get_password()
        token = login(user.username, password)
    if not to_signup and not to_remember:
        token = login(**data_from_login())

    header = {"Authorization": "Bearer " + token}
    print(user)
    print(header)


if __name__ == "__main__":
    runner_main(to_signup=True)
