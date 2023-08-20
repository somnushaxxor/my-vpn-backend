from fastapi import FastAPI
from get_profile import get_profile_router

app = FastAPI()

app.include_router(get_profile_router)
