from fastapi import FastAPI
from Server.route import router

app = FastAPI()

app.include_router(router)
