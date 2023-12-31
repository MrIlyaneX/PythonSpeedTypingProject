""" DataBase class represents user data, statistics for exchange between Client-Server """
from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class Stats(BaseModel):
    """
    Stats used by the User in Client-Server exchange
     """
    max_score: int = 0
    avg_accuracy: float | None = None
    time_spend: float | None = None
    last_visit: datetime | None = datetime.utcnow()
    max_symbols_per_day: int | None = None


class User(BaseModel):
    """
    Data class represents the model of User data which Server-Client exchange
    """
    username: str
    email: str | None = None
    disabled: bool | None = False
    achievements: Stats | None = None


class Token(BaseModel):
    """
    Represents token
    """
    access_token: str
    remember_token: str | None
    token_type: str


class TokenData(BaseModel):
    """
    Class represents token data
    """
    username: str | None = None


class Language(str, Enum):
    """
    Enum class represents acceptable languages for the application
    """
    ru = "ru"
    en = "en"
