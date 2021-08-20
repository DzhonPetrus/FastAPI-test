from fastapi import status, HTTPException
from sqlalchemy.orm import Session

from .. import models
from ..helpers.hashing import Hash

def get_all(db: Session):
    users = db.query(models.User).all()
    return users

def get_one(id, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id} not found')
    return user

def create(user, db: Session):
    new_user = models.User(name=user.name, email=user.email, password=Hash.bcrypt(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user