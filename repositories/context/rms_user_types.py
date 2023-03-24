import uuid
from typing import Dict

from sqlalchemy.orm import Session

from dto.context.rms_user_types import RmsUserTypesShow
from models.context.rms_user_types import RmsUserTypes
from dto.context import rms_user_types


class RmsUserTypeDAL:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_rms_user_types(self, rms_user_types: rms_user_types.RmsUserTypesCreate) -> Dict:
        db_rms_user_types = RmsUserTypes(name=rms_user_types.name, description=rms_user_types.description,
                                         list_order=rms_user_types.list_order)
        self.db_session.add(db_rms_user_types)
        self.db_session.commit()
        self.db_session.refresh(db_rms_user_types)
        return {"name": rms_user_types.name, "description": rms_user_types.description,
                "list_order": rms_user_types.list_order}

    def get_rms_user_types(self, user_id: uuid.UUID) -> RmsUserTypesShow:
        return self.db_session.query(RmsUserTypes).filter(RmsUserTypes.id == user_id).first()

    def get_rms_user_types_by_name(self, name: str) -> RmsUserTypesShow:
        return self.db_session.query(RmsUserTypes).filter(RmsUserTypes.name == name).first()
