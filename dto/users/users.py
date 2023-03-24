from pydantic import BaseModel
import uuid


class User(BaseModel):
    id: uuid

    class Config:
        orm_mode = True
