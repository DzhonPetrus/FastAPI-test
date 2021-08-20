from fastapi import status, HTTPException
from sqlalchemy.orm import Session

from .. import models, schemas



def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def get_one(id, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not found')
    return blog


def create(blog: schemas.Blog, db: Session):
    new_blog = models.Blog(title=blog.title, body = blog.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def destroy(id, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    else:
        blog.delete(synchronize_session=False)
        db.commit()
        return {
            'detail': f'Blog with id {id} deleted'
        }


def update(id, blog: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not found')

    else:
        update({'title': blog.title, 'body': blog.body})
        db.commit()
        return {
            'data': blog,
            'detail': f'Blog with id {id} updated'
        }



