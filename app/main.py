from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.articles.router import router as articles_router
from app.users.router import router as users_router
from app.pages.router import router as pages_router
from app.images.router import router as images_router

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), "static")

app.include_router(users_router)
app.include_router(articles_router)
app.include_router(pages_router)
app.include_router(images_router)
