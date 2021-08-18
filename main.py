from fastapi import FastAPI
from typing import Optional, Text
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get('/blog')
def index(limit: int = 25, published: bool = True, sort: Optional[str] = None):
    # only get 10 published blogs
    if published:
        return { 'data': f'{limit} published blogs from db' }
    else:
        return { 'data': f'{limit} all blogs from db' }

@app.get('/blog/unpublished')
def getUnpublished():
    return {
        'data': {
            'id': 0

        }
    }

# STATIC ROUTE MUST BE DEFINED BEFORE DYNAMIC ROUTE

@app.get('/blog/{id}')
def getOne(id: int):
    return {
        'data': {
            'id': 0
        }
    }

@app.get('/blog/{id}/comments')
def comments(id: int, limit=10):
    return {
        'data': {
            'id': 0,
            'text': 'nice'
        }
    }

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]



@app.post('/blog')
def createBlog(blog: Blog):
    return {
        "data": f'Blog {blog}'
    }



# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)