from datetime import timedelta
from typing import Annotated

from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt

from db.data_classes import *
from Server.config import pwd_context, SECRET_KEY, ALGORITHM, oauth2_scheme
from Server.db_access import get_user


def verify_password(plain_password, hashed_password) -> bool:
    """
    Verifies if the plain password matches the hashed password.
    
    :param plain_password: The plain password to verify.
    :param hashed_password: The hashed password to compare against.
    :return: True if the passwords match, False otherwise.
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password) -> str:
    """
    Hashes the provided password.

    :param password: The password to hash.
    :return: The hashed password.
    """
    return pwd_context.hash(password)


def authenticate_user(username: str, password: str) -> UserInDB | bool:
    """
    Authenticates the user with the provided username and password.

    :param username: The username of the user.
    :param password: The password of the user.
    :return: The User object if authentication is successful, False otherwise.
    """
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """
    Creates an access token with the provided data.

    :param data: The data to include in the token.
    :param expires_delta: Optional timedelta for token expiration.
    :return: The encoded access token.
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> UserInDB:
    """
    Retrieves the current user based on the provided access token.

    :param token: The access token passed in the request header.
    :return: The User object corresponding to the token.

    :raises HTTPException: If the token is invalid or the user does not exist.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(
        current_user: Annotated[UserInDB, Depends(get_current_user)]
) -> UserInDB:
    """
    Retrieves the current active user based on the provided current user.

    :param current_user: The current user object.
    :return: The current active user.

    :raises HTTPException: If the current user is disabled.
    """
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
