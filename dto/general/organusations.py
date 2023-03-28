import uuid
from datetime import datetime
from typing import Union, Text

from pydantic import BaseModel


class Organisations(BaseModel):
    default_name: Union[str, None]
    ror_id: Union[int, None]
    display_suffix: Union[str, None]
    scope_id: Union[int, None]
    scope_notes: Text | None
    is_current: bool = True
    year_established: Union[int, None]
    year_ceased: Union[int, None]
    city: Union[str, None]
    country_name: Union[str, None]
    created_on: datetime


class OrganisationsCreate(Organisations):
    pass


class OrganisationsShow(Organisations):
    id = uuid.UUID

    class Config:
        orm_mode = True
