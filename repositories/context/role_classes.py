import uuid
from typing import Dict

from sqlalchemy.orm import Session

from dto.context.rms_user_types import RmsUserTypesShow
from models.context.role_classes import RoleClasses
from dto.context import role_classes


class RoleClassesTypeDAL:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_role_classes(self, role_classes: role_classes.RoleClassesCreate) -> Dict:
        db_role_classes = RoleClasses(name=role_classes.name, description=role_classes.description,
                                         list_order=role_classes.list_order)
        self.db_session.add(db_role_classes)
        self.db_session.commit()
        self.db_session.refresh(db_role_classes)
        return {"name": role_classes.name, "description": role_classes.description,
                "list_order": role_classes.list_order}

    def get_role_classes(self, user_id: uuid.UUID) -> RmsUserTypesShow:
        return self.db_session.query(RoleClasses).filter(RoleClasses.id == user_id).first()

    def get_role_classes_by_name(self, name: str) -> RmsUserTypesShow:
        return self.db_session.query(RoleClasses).filter(RoleClasses.name == name).first()
