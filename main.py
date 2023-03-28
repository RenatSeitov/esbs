from fastapi import FastAPI
from routers.context import rms_user_types, role_classes, role_types


app = FastAPI()


app.include_router(rms_user_types.router)
app.include_router(role_classes.router)
app.include_router(role_types.router)

