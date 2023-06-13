from pydantic import BaseModel


class UserInfo(BaseModel):
    name: str
    id: int
