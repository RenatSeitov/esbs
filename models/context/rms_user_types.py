import uuid

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, Text, Integer

from database.database import Base


class RmsUserTypes(Base):
    __tablename__ = 'rms_user_types'

    id = Column(UUID(as_uuid=True), index=True, default=uuid.uuid4, unique=True)
    name = Column(String(75), unique=True, index=True)
    description = Column(Text, nullable=True)
    list_order = Column(Integer, default=0)

    __table_args__ = {"rms_user_types": "list_order"}
