from fastapi import FastAPI

from client_server_api.DB import *

app = FastAPI()

user_data = {}


@app.post("/user/{link}")
def post_user_info(link: str, user_info: UserInfo):
    user_data[link] = user_info.dict()
    return {"message": "User info posted successfully", "info": user_data[link]}



@app.get("/user/{link}")
def get_user_info(link: str):
    if link in user_data:
        return {"info": user_data[link]}
    else:
        return {"message": "User info not found"}
