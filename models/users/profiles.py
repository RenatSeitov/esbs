import uuid
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from database.database import Base
from models.context.rms_user_types import RmsUserTypes
from models.context.role_classes import RoleClasses
from models.context.role_types import RoleTypes
from models.general.organisations import Organisations
from users import Users


class UserProfiles(Base):
    __tablename__ = 'user_profiles'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey(Users.id), unique=True, nullable=False)
    role_id = Column(UUID(as_uuid=True), ForeignKey(RoleTypes.id), nullable=False)
    role_class_id = Column(UUID(as_uuid=True), ForeignKey(RoleClasses.id), nullable=False)
    user_type_id = Column(UUID(as_uuid=True), ForeignKey(RmsUserTypes.id), nullable=False)
    organisation_id = Column(UUID(as_uuid=True), ForeignKey(Organisations.id), nullable=False)

    ls_aai_id = Column(String(255))
    user = relationship(Users, backref='user_profiles_user_id')
    role = relationship(RoleTypes, backref='users_role_id')
    role_class = relationship(RoleClasses, backref='users_role_class')
    user_type = relationship(RmsUserTypes, backref='users_user_type')
    organisation = relationship(Organisations, backref='users_organisation_id')
