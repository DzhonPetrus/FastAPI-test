from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session


from .. import schemas, database, models
from ..controllers import blog

router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)

get_db = database.get_db


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db)):
    return blog.get_all(db)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def one(id, db: Session = Depends(get_db)):
    return blog.get_one(id, db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(Blog: schemas.Blog, db: Session = Depends(get_db)):
    return blog.create(Blog, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db)):
    return blog.destroy(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, Blog: schemas.Blog, db: Session = Depends(get_db)):
    return blog.update(id, Blog, db)
