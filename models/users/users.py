import uuid

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column

from database.database import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
