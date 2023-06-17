from datetime import datetime
from getpass import getpass

import requests

from client import get_token, get_user_info, post_user_info, signup
from DB import *

server_url = "http://127.0.0.1:8000"

if __name__ == "__main__":
    user_info = UserInfo(
        ids=1,
        name="John",
        email="john@example.com",
        password="password",
        registration_date="2023-06-17T12:00:00",
    )

    # Signup user
    signup_status = signup(user_info)
    if signup_status == 200:
        print("User signup successful")
    else:
        print("User signup failed")
        exit(1)

    # User information to post
    info_to_post = UserInfo(
        ids=1,
        name="John",
        email="john@example.com",
        password="password",
        registration_date=datetime.now(),
    )

    # Get token for authentication
    token = get_token("John", SecretStr("password"))

    # Post user information
    post_response = post_user_info(info_to_post, link=1, token=token)
    print("Post response:", post_response)

    # Get user information
    get_response = get_user_info(link=1, token=token)
    print("Get response:", get_response)
