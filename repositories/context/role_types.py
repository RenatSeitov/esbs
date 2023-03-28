import uuid
from typing import Dict

from sqlalchemy.orm import Session

from dto.context.role_types import RoleTypeShow
from models.context.role_types import RoleTypes
from dto.context import role_types


class RoleTypeDAL:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_role_type(self, role_t: role_types.RoleTypeCreate) -> Dict:
        db_role_type = RoleTypes(name=role_t.name, list_order=role_t.list_order, role_class_id=role_t.role_class_id)
        self.db_session.add(db_role_type)
        self.db_session.commit()
        self.db_session.refresh(db_role_type)
        return {"name": role_t.name, "list_order": role_t.list_order}

    def get_role_types(self, user_id: uuid.UUID) -> RoleTypeShow:
        return self.db_session.query(RoleTypes).filter(RoleTypes.id == user_id).first()

    def get_role_type_by_name(self, name: str) -> RoleTypeShow:
        return self.db_session.query(RoleTypes).filter(RoleTypes.name == name).first()
