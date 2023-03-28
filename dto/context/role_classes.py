import uuid
from typing import Text, Union

from pydantic import BaseModel


class RoleClassesBase(BaseModel):
    name: str
    description: Text
    list_order: Union[int, None]


class RoleClassesCreate(RoleClassesBase):
    pass


class RoleClassesShow(RoleClassesBase):
    id: uuid.UUID

    class Config:
        orm_mode = True
