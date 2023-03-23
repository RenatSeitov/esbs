import uuid

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, Integer, ForeignKey

from database.database import Base
from role_classes import RoleClasses
from sqlalchemy.orm import relationship


class RoleTypes(Base):
    __tablename__ = "role_types"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, index=True)
    name = Column(String(75), unique=True, index=True)
    list_order = Column(Integer, default=0)
    role_class_id = Column(UUID(as_uuid=True), ForeignKey(RoleClasses.id), index=True)
    role_class = relationship(RoleClasses, backref="role_types")

    __table_args__ = {"role_types": "list_order"}
