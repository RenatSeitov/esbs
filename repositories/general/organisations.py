import uuid
from typing import Dict

from sqlalchemy.orm import Session

from dto.general.organusations import OrganisationsShow
from models.general.organisations import Organisations
from dto.general import organusations


class OrganisationsDAL:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_organisation(self, organisation: organusations.OrganisationsCreate) -> Dict:
        db_role_classes = Organisations(default_name=organisation.default_name, ror_id=organisation.ror_id,
                                        display_suffix=organisation.display_suffix, scope_id=organisation.scope_id,
                                        scope_notes=organisation.scope_notes, is_current=organisation.is_current,
                                        year_established=organisation.year_established, year_ceased=organisation.year_ceased,
                                        city=organisation.city, country_name=organisation.country_name, created_on=organisation.created_on)
        self.db_session.add(db_role_classes)
        self.db_session.commit()
        self.db_session.refresh(db_role_classes)
        return {"default_name": organisation.default_name, "display_suffix": organisation.display_suffix,
                "city": organisation.city}

    def get_organisations(self, user_id: uuid.UUID) -> OrganisationsShow:
        return self.db_session.query(Organisations).filter(Organisations.id == user_id).first()

    def get_organisation_by_name(self, default_name: str) -> OrganisationsShow:
        return self.db_session.query(Organisations).filter(Organisations.default_name == default_name).first()
