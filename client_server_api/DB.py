""" DataBase class represents user data, statistics """
from typing import Optional
from pydantic import BaseModel, EmailStr, Field, SecretStr
from datetime import datetime


class Stats(BaseModel):
    ids: int = Field(..., description="User ID")
    max_score: int
    avg_accuracy: float
    level: int
    max_speed_accuracy: float
    days_in_row: Optional[int] = 0
    time_spend: Optional[float] = 0
    last_visit: Optional[datetime] = None
    max_symbols_per_day: int


class UserInfo(BaseModel):
    """ Data class made with pydantic"""
    ids: int = Field(..., description="User ID")
    name: str = Field(..., description="User name")
    email: EmailStr = Field(..., description="Email address of the user", example="example@example.com")
    password: SecretStr = Field(..., description="Password of the user")
    registration_date: datetime = Field(datetime.now(), description="Registration date of the user",
                                        example=datetime.now())

    achievements: Optional[Stats] = None
