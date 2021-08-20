
from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from .. import schemas, database

from ..controllers import user

router = APIRouter(
    prefix="/user",
    tags=['Users']
)

get_db = database.get_db


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create(User: schemas.User, db: Session = Depends(get_db)):
    return user.create(User, db)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def show(id, db: Session = Depends(get_db)):
    return user.get_one(id, db)

@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowUser])
def all(db: Session = Depends(get_db)):
    return user.get_all(db)