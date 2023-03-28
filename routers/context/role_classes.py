import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.db_factory import get_db
from dto.context import role_classes
from repositories.context.role_classes import RoleClassesTypeDAL

router = APIRouter(
    prefix="/role_classes",
    tags=["role_classes"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=role_classes.RoleClassesCreate)
def create_role_classes(role_cl: role_classes.RoleClassesCreate, db: Session = Depends(get_db)):
    user_types = RoleClassesTypeDAL(db).get_role_classes_by_name(name=role_cl.name)
    if user_types:
        raise HTTPException(status_code=400, detail="Class already registered")
    return RoleClassesTypeDAL(db).create_role_classes(role_classes=role_cl)


@router.get("/", response_model=role_classes.RoleClassesShow)
def read_role_classes(name: str, db: Session = Depends(get_db)):
    role_classes = RoleClassesTypeDAL(db).get_role_classes_by_name(name=name)
    if role_classes is None:
        raise HTTPException(status_code=404, detail="Class not found")
    return role_classes


@router.get("/{user_uuid}", response_model=role_classes.RoleClassesShow)
def read_rms_user_types(user_id: uuid.UUID, db: Session = Depends(get_db)):
    db_user = RoleClassesTypeDAL(db).get_role_classes(user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Class not found")
    return db_user
