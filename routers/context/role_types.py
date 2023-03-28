import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.db_factory import get_db
from dto.context import role_types
from repositories.context.role_types import RoleTypeDAL

router = APIRouter(
    prefix="/role_types",
    tags=["role_types"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=role_types.RoleTypeCreate)
def create_role_type(role_t: role_types.RoleTypeCreate, db: Session = Depends(get_db)):
    user_types = RoleTypeDAL(db).get_role_type_by_name(name=role_t.name)
    if user_types:
        raise HTTPException(status_code=400, detail="Class already registered")
    return RoleTypeDAL(db).create_role_type(role_t=role_t)


@router.get("/", response_model=role_types.RoleTypeShow)
def read_role_types(name: str, db: Session = Depends(get_db)):
    role_classes = RoleTypeDAL(db).get_role_type_by_name(name=name)
    if role_classes is None:
        raise HTTPException(status_code=404, detail="Class not found")
    return role_classes


@router.get("/{user_uuid}", response_model=role_types.RoleTypeShow)
def read_role_types(user_id: uuid.UUID, db: Session = Depends(get_db)):
    db_user = RoleTypeDAL(db).get_role_types(user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Class not found")
    return db_user
