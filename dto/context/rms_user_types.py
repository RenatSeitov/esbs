import uuid
from typing import Text, Union

from pydantic import BaseModel


class RmsUserTypesBase(BaseModel):
    name: str
    description: Text
    list_order: Union[int, None]


class RmsUserTypesCreate(RmsUserTypesBase):
    pass


class RmsUserTypesShow(RmsUserTypesBase):
    id: uuid.UUID

    class Config:
        orm_mode = True
