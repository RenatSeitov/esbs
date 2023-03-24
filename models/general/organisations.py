import uuid
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, Integer, Text, Boolean, DateTime

from database.database import Base


class Organisations(Base):
    __tablename__ = "organisations"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4, unique=True)
    default_name = Column(String(255), unique=True,  index=True)
    ror_id = Column(Integer, unique=True, index=True, nullable=True)
    display_suffix = Column(String(255), index=True, nullable=True)
    scope_id = Column(Integer, index=True, nullable=True)
    scope_notes = Column(Text, nullable=True)
    is_current = Column(Boolean, index=True, default=True)
    year_established = Column(Integer, nullable=True, index=True)
    year_ceased = Column(Integer, nullable=True, index=True)
    city = Column(String(255), nullable=True, index=True)
    country_name = Column(String(255), nullable=True, index=True)
    created_on = Column(DateTime, default=datetime.utcnow)
