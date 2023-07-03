from fastapi import FastAPI
from Server.route import router as main_router

app = FastAPI()

app.include_router(router=main_router)
