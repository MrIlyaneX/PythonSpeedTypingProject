""" Works with client data exchange to server and inner data """

from Client.client import signup, login, upload_info, get_info
from Client.models.data_classes import User, Token

server_url = "http://127.0.0.1:8000"


def get_header(username: str, password: str, user_email: str, to_login: bool | None = None,
               to_signup: bool | None = None, to_remember: bool = False) -> dict | None:
    """
    Main function for client actions
    SignUp or LogIn user into system and returns header with token or None if error occurred

    :param username: username
    :param password: password
    :param user_email: email
    :param to_login: if True, login
    :param to_signup: if True, signup
    :param to_remember: if True, remember
    :return: None or Header
    """

    token: dict | Token | None = None

    if to_signup:
        status = signup(username, password, user_email)
        if isinstance(status, User):
            token = login(username, password)
        else:
            return None
    if to_login and not to_remember:
        token = login(username, password)
    if to_login and to_remember:
        token = login(username, password)

    if token is not None:
        if "msg" in token.keys():
            return None
        print(token)
        tokens = Token(**token)
        return {"Authorization": "Bearer " + tokens.access_token}
    else:
        return None


def get_user(header: dict) -> User | None:
    """
    Gets user using auth header

    :param header: header
    :return: user of type User
    """
    return get_info(header)


def get_achievements(header: dict) -> dict | None:
    """
    Gets user achievements using auth header

    :param header: header
    :return: user achievements
    """
    return get_info(header).achievements.dict()


# I need to use functions from client.py for easy use of client part
def upload_user_info(header: dict, user: User) -> None:
    """
    Uploads user info to server

    :param header: header
    :param user: user info
    :return: None
    """
    upload_info(header=header, user_info=user)


def main():
    """ Actions for testing the work of system (server+app) """
    header = get_header(to_signup=True, password="123",
                        username="loasdq2", user_email="123")
    print(header)
    user = get_user(header)
    achievements = get_achievements(header)
    print(user)
    print(achievements)


if __name__ == "__main__":
    main()
