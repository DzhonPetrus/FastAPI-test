from datetime import timedelta

from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from blog.jwt_token import ACCESS_TOKEN_EXPIRE_MINUTES
from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session


from .. import schemas, database, models, jwt_token
from ..helpers import hashing


router = APIRouter(
    tags=['Authentication']
)

@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Invalid credentials')
    
    if hashing.Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Incorrect password')

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = jwt_token.create_access_token(
        data={
            "id": user.id,
            "email": user.email,
            "exp": access_token_expires
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
