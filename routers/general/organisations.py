import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.db_factory import get_db
from dto.general import organusations
from repositories.general.organisations import OrganisationsDAL

router = APIRouter(
    prefix="/organisation",
    tags=["organisation"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=organusations.OrganisationsCreate)
def create_organisation(org: organusations.OrganisationsCreate, db: Session = Depends(get_db)):
    organisation = OrganisationsDAL(db).get_organisation_by_name(default_name=org.default_name)
    if organisation:
        raise HTTPException(status_code=400, detail="Organisation already registered")
    return OrganisationsDAL(db).create_organisation(organisation=org)


@router.get("/", response_model=organusations.OrganisationsShow)
def read_organisation(name: str, db: Session = Depends(get_db)):
    organisation = OrganisationsDAL(db).get_organisation_by_name(default_name=name)
    if organisation is None:
        raise HTTPException(status_code=404, detail="Organisation not found")
    return organisation


@router.get("/{user_uuid}", response_model=organusations.OrganisationsShow)
def read_organisations(user_id: uuid.UUID, db: Session = Depends(get_db)):
    organisation = OrganisationsDAL(db).get_organisations(user_id=user_id)
    if organisation is None:
        raise HTTPException(status_code=404, detail="Organisation not found")
    return organisation
