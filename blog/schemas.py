from typing import List, Optional
from pydantic import BaseModel


class Base(BaseModel):
    class Config():
        orm_mode = True

class Blog(Base):
    title: str
    body: str

class User(Base):
    name: str
    email: str
    password: str

class ShowUser(User):
    blogs: List[Blog] = []

class ShowBlog(Blog):
    creator: ShowUser


class Login(Base):
    email: str
    password: str



class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None
    email: Optional[str] = None