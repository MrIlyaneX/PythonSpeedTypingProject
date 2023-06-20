""" DataBase class represents user data, statistics """
from enum import Enum
from pydantic import BaseModel
from datetime import datetime


class Stats(BaseModel):
    max_score: int = 0
    avg_accuracy: float | None = None
    max_speed_accuracy: float | None = None
    last_visit: datetime | None = datetime.utcnow()
    max_symbols_per_day: int | None = None


class User(BaseModel):
    username: str
    email: str | None = None
    disabled: bool | None = False
    achievements: Stats | None = None


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class UserInDB(User):
    hashed_password: str


class Language(str, Enum):
    ru = "ru"
    en = "en"
