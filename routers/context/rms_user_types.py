import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.db_factory import get_db
from dto.context import rms_user_types
from repositories.context.rms_user_types import RmsUserTypeDAL

router = APIRouter(
    prefix="/rms_user_types",
    tags=["rms_user_types"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=rms_user_types.RmsUserTypesCreate)
def create_rms_user_types(rms_user_types: rms_user_types.RmsUserTypesCreate, db: Session = Depends(get_db)):
    user_types = RmsUserTypeDAL(db).get_rms_user_types_by_name(name=rms_user_types.name)
    if user_types:
        raise HTTPException(status_code=400, detail="Type already registered")
    return RmsUserTypeDAL(db).create_rms_user_types(rms_user_types=rms_user_types)


@router.get("/", response_model=rms_user_types.RmsUserTypesShow)
def read_rms_user_types(name: str, db: Session = Depends(get_db)):
    rms_user_types = RmsUserTypeDAL(db).get_rms_user_types_by_name(name=name)
    if rms_user_types is None:
        raise HTTPException(status_code=404, detail="Type not found")
    return rms_user_types


@router.get("/{user_uuid}", response_model=rms_user_types.RmsUserTypesShow)
def read_rms_user_types(user_id: uuid.UUID, db: Session = Depends(get_db)):
    db_user = RmsUserTypeDAL(db).get_rms_user_types(user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Type not found")
    return db_user
