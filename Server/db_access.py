from database.db import *

from db.data_classes import *


def get_user(username: str):
    """
    Retrieves the user with the specified username.
    :param username: The username of the user to retrieve.
    :return: The UserInDB object if the user exists, None otherwise.
    """
    user = get_person_by_username(username=username)
    if user is not None:
        return UserInDB(**user)


def update_user_achievements(user: User):
    """
    Updates the user's achievements in the database.
    :param user: The User object containing the updated achievements.
    """
    set_achieve(data=user.achievements.dict(), name=user.username)
