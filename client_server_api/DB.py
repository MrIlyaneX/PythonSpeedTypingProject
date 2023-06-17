""" DataBase class represents user data, statistics """
from typing import Optional
from pydantic import BaseModel, EmailStr, Field, SecretStr
from datetime import datetime


class Stats(BaseModel):
    ids: int
    max_score: int = 0
    avg_accuracy: float | None = None
    level: int = 0
    max_speed_accuracy: float | None = None
    days_in_row: int = 0
    time_spend: float = 0
    last_visit: datetime | None = None
    max_symbols_per_day: int | None = None


class User(BaseModel):
    username: str
    ids: int
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None
    registration_date: datetime | None = datetime.utcnow()
    achievements: Stats | None = None


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class UserInDB(User):
    hashed_password: str
