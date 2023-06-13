from pydantic import BaseModel, EmailStr, Field
from datetime import datetime


class UserInfo(BaseModel):
    id: int = Field(..., description="User ID")
    name: str = Field(..., description="User name")
    email: EmailStr = Field(..., description="Email address of the user", example="example@example.com")
    registration_date: datetime = Field(datetime.now(), description="Registration date of the user",
                                        example=datetime.now())

    achievements: dict
    last_visit: datetime
    days_in_row: int

    # 'game' stats
    max_score: int
    avg_accuracy: float
    level: int
