
from typing import List
from fastapi import APIRouter, Depends, status, Request
from sqlalchemy.orm import Session

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from .. import schemas, database

from ..controllers import user



templates = Jinja2Templates(directory="blog/templates")

router = APIRouter(
    prefix="/user",
    tags=['Users']
)

get_db = database.get_db


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create(User: schemas.User, db: Session = Depends(get_db)):
    return user.create(User, db)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def show(request: Request, id, db: Session = Depends(get_db)):
    # return user.get_one(id, db)
    return templates.TemplateResponse("user.html", {"request":request, "user": user.get_one(id, db)})

@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowUser], response_class=HTMLResponse)
def all(request: Request, db: Session = Depends(get_db)):
    # return user.get_all(db)
    return templates.TemplateResponse("users.html", {"request":request, "users": user.get_all(db)})