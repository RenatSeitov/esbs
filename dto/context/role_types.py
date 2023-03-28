import uuid
from typing import Union

from pydantic import BaseModel


class RoleType(BaseModel):
    name: str
    list_order: Union[int, None]
    role_class_id: uuid.UUID


class RoleTypeCreate(RoleType):
    pass


class RoleTypeShow(RoleType):
    id: uuid.UUID

    class Config:
        orm_mode = True
