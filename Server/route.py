from datetime import timedelta
from typing import Annotated

from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.responses import FileResponse
from fastapi.security import OAuth2PasswordRequestForm
from starlette.responses import HTMLResponse

from Server.auth_functions import create_access_token, authenticate_user, get_current_active_user, get_password_hash
from Server.config import ACCESS_TOKEN_EXPIRE_MINUTES
<<<<<<< HEAD
from Server.db_access import get_person_by_username, update_user_achievements, add_person, get_leaderboard
from db.data_classes import Token, User, Language
=======
from Server.models.db_access import get_person_by_username, update_user_achievements, get_leaderboard
from Server.models.data_classes import Token, User, Language
from Server.models.db import add_person
>>>>>>> feature-setup-wizard

router = APIRouter()


@router.post("/token", response_model=Token)
async def login_for_access_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> dict:
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
) -> User:
    """
    Retrieve the details of the current authenticated user.

    :param current_user: The currently authenticated user.
    :return: The details of the current user as a dictionary.
    """
    return current_user


@router.post("/users/me/upload", response_model=dict)
async def upload_own_data(
        current_user: Annotated[User, Depends(get_current_active_user)], user: User
) -> dict:
    """
    Upload data for the current authenticated user.

    :param current_user: The currently authenticated user.
    :param user: The user data to be uploaded.
    :return: A dictionary indicating the success of the upload.

    :raises HTTPException: The username is already registered.
    """
    if get_person_by_username(username=user.username) is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username do not exist",
        )

    update_user_achievements(user=user)
    return {"Success": True}


@router.post("/signup", response_model=User)
async def signup(username: str, user_email: str, password: str) -> User:
    """
    Sign up a new user.

    :param username: The username for the new user.
    :param user_email: The user data to be signed up.
    :param password: The password for the new user.
    :return: The signed-up user details.

    :raises HTTPException: If the username is already registered.
    """
    if get_person_by_username(username=username) is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered",
        )
    hashed_password = get_password_hash(password)

    add_person(username=username, password=hashed_password, mail=user_email)
    return User(**get_person_by_username(username=username))


@router.get("/files/words/{language}")
async def send_words(language: Language) -> FileResponse:
    """
    Retrieve words for a specific language.

    :param language: The language for which words are requested.
    :return: The file containing words in the specified language.

    :raises HTTPException: If the language is invalid.
    """
    if language == Language.en:
        return FileResponse("Server/words/en.json", media_type="application/json", filename="en.json")
    elif language == Language.ru:
        return FileResponse("Server/words/en.json", media_type="application/json", filename="en.json")
    else:
        raise HTTPException(
            status_code=400,
            detail="Invalid language"
        )


@router.post("/leaderboard", response_model=dict)
async def post_leaderboard() -> dict:
    return get_leaderboard()


@router.get("/download")
async def app_download() -> FileResponse:
    file_path = "Server/static/run_client_app.exe"
    return FileResponse(file_path, media_type="application/octet-stream", filename="ty-typing.exe")


@router.get("/")
async def index() -> HTMLResponse:
    with open("Server/static/html/download.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content, status_code=200)