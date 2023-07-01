from datetime import timedelta
from typing import Annotated

import aiofiles
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.responses import FileResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext

from db.data_classes import *

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

fake_users_db = {
    "johndoe": {
        "ids": 1,
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
        "achievements": {
            "ids": 1,
            "max_score": 100,
            "avg_accuracy": 0.9,
            "level": 5,
            "max_speed_accuracy": 0.8,
            "days_in_row": 10,
            "time_spend": 8.5,
            "last_visit": "2022-06-01T10:00:00",
            "max_symbols_per_day": 500
        },
    }
}

keys = ["max_score", "avg_accuracy", "level", "max_speed_accuracy", "days_in_row", "time_spend", "last_visit",
        "max_symbols_per_day"]

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


<<<<<<< HEAD

@app.get("/user/{link}")
def get_user_info(link: str):
    if link in user_data:
        return {"info": user_data[link]}
=======
def get_user(db, username: str):
    if username in db:
        return UserInDB(**db[username])


def update_user_achievements(db, username: str, user: User, db_user: UserInDB):
    db_user_copy = db_user.copy().dict()
    user_copy = user.copy().dict()
    if username in db:
        for key in keys:
            if db_user_copy["achievements"][key] != user_copy["achievements"][key]:
                db_user_copy["achievements"][key] = user_copy["achievements"][key]
        db[username] = UserInDB(**db_user_copy)


def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
>>>>>>> origin/master
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
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
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(
        current_user: Annotated[User, Depends(get_current_user)]
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@app.post("/token", response_model=Token)
async def login_for_access_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
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


@app.get("/users/me/", response_model=User)
async def read_users_me(
        current_user: Annotated[User, Depends(get_current_active_user)]
):
    return current_user.dict()


@app.post("/users/me/upload")
async def upload_own_data(
        current_user: Annotated[User, Depends(get_current_active_user)], user: User
):
    db_user = get_user(fake_users_db, current_user.username)
    update_user_achievements(db=fake_users_db, username=current_user.username, user=user, db_user=db_user)

    # Code for testing database data
    # async with aiofiles.open("users.txt", mode="w") as users:
    #     for us in fake_users_db:
    #         await users.write(str(fake_users_db[us]) + "\n")
    return {"Success": True}


@app.post("/signup", response_model=User)
async def signup(user: User, password: str):
    if user.username in fake_users_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered",
        )
    hashed_password = get_password_hash(password)
    user_to_pass = user.copy()
    user_to_pass.achievements = user_to_pass.achievements.dict()
    user_data = user_to_pass.dict()
    user_data["hashed_password"] = hashed_password
    fake_users_db[user.username] = user_data
    return user_to_pass


@app.get("/files/words/{language}")
async def send_words(language: Language):
    if language in Language.en:
        return FileResponse("Server/words/en.json", media_type="application/json", filename="en.json")
    if language is Language.ru:
        pass
    raise HTTPException(status_code=400, detail="Invalid language")