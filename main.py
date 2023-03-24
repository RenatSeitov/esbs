from fastapi import FastAPI
from routers.context import rms_user_types


app = FastAPI()


app.include_router(rms_user_types.router)

