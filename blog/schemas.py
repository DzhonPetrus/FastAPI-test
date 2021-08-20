from typing import List
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

