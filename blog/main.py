from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from . import models, routers
from .database import engine
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(engine)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

app.mount("/static", StaticFiles(directory="blog/static"), name="static")


app.include_router(routers.authentication.router)
app.include_router(routers.blog.router)
app.include_router(routers.user.router)