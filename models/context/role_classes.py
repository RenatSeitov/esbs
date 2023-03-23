import uuid

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, Text, Integer

from database.database import Base


class RoleClasses(Base):
    __tablename__ = "role_classes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, index=True)
    name = Column(String(75), unique=True, index=True)
    description = Column(Text, nullable=True)
    list_order = Column(Integer, default=0)

    __table_args__ = {"role_classes": "list_order"}
