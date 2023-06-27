from datetime import timedelta
from typing import Annotated

from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.responses import FileResponse
from fastapi.security import OAuth2PasswordRequestForm

from Server.config import ACCESS_TOKEN_EXPIRE_MINUTES
from Server.auth_functions import create_access_token, authenticate_user, get_current_active_user, get_password_hash
from Server.db_access import get_person_by_username, update_user_achievements, add_person
from db.data_classes import Token, User, Language

router = APIRouter()


@router.post("/token", response_model=Token)
async def login_for_access_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    """
    Retrieves an access token for the user based on the provided login credentials.
    :param form_data: The login form data.
    :return: The access token.
    :raises HTTPException: If the username or password is incorrect.
    """
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/users/me/", response_model=User)
async def read_users_me(
        current_user: Annotated[User, Depends(get_current_active_user)]
):
    """
    Retrieve the details of the current authenticated user.
    :param current_user: The currently authenticated user.
    :return: The details of the current user as a dictionary.
    """
    return current_user.dict()


@router.post("/users/me/upload")
async def upload_own_data(
        current_user: Annotated[User, Depends(get_current_active_user)], user: User
):
    """
    Upload data for the current authenticated user.
    :param current_user: The currently authenticated user.
    :param user: The user data to be uploaded.
    :return: A dictionary indicating the success of the upload.
    :raises HTTPException: If the username is already registered.
    """
    if get_person_by_username(username=user.username) is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username do not exist",
        )
    update_user_achievements(username=current_user.username, user=user)
    return {"Success": True}


@router.post("/signup", response_model=User)
async def signup(user: User, password: str):
    """
    Sign up a new user.
    :param user: The user data to be signed up.
    :param password: The password for the new user.
    :return: The signed-up user details.
    :raises HTTPException: If the username is already registered.
    """
    if get_person_by_username(username=user.username) is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered",
        )
    hashed_password = get_password_hash(password)
    user_to_pass = user.copy()

    add_person(username=user.username, password=hashed_password, mail=user.email)

    return user_to_pass


@router.get("/files/words/{language}")
async def send_words(language: Language):
    """
    Retrieve words for a specific language.
    :param language: The language for which words are requested.
    :return: The file containing words in the specified language.
    :raises HTTPException: If the language is invalid.
    """
    if language in Language.en:
        return FileResponse("Server/words/en.json", media_type="application/json", filename="en.json")
    if language is Language.ru:
        pass
    raise HTTPException(status_code=400, detail="Invalid language")
