""" Starter code for api-server part for the database """
import hashlib
from typing import List

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt
from passlib.context import CryptContext

from client_server_api.DB import *

app = FastAPI()

user_data = []
SECRET_KEY = "secret-key"  # key fo tokens
oauth = OAuth2PasswordBearer(tokenUrl="/user/login")

# schemes=["bcrypt"] -- password hashing schema
# deprecated="auto"  -- automatic management of hashing schema level
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    return hash_password(password) == hashed_password


def authenticate_user(credentials: OAuth2PasswordRequestForm):
    username = credentials.username
    password = credentials.password

    user = next((user for user in user_data if user.name == username), None)

    if user and verify_password(password, user.password.get_secret_value()):
        return user.ids

    return None


def create_access_token(user_id: int):
    return jwt.encode({"user_id": user_id}, SECRET_KEY, algorithm="HS256")


@app.post("/user/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(oauth)):
    user_id = authenticate_user(form_data)
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token = create_access_token(user_id)
    return {"access_token": token, "token_type": "bearer"}


@app.get("/user/signup")
def signup(user: UserInfo):
    user.password = hash_password(user.password.get_secret_value())
    user_data.append(user)

    return {"message": "User signed up successfully", "user": user}


@app.get("/user/{link}")
def get_user_info(link: str, token: str = Depends(oauth)):
    try:
        info = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        user_id = info.get("ids")
        user = next((user for user in user_data if user.ids == user_id), None)

        if user:
            return {"info": user}
        else:
            return {"message": "User info not found"}

    except jwt.JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )


@app.post("/user/{link}")
def post_user_info(link: str, user_info: UserInfo, token: str = Depends(oauth)):
    try:
        info = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        user_id = info.get("ids")

        user = next((user for user in user_data if user.ids == user_id), None)
        return {"message": "User info posted successfully", "info": user}
    except jwt.JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )
