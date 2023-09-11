from fastapi import FastAPI

from app.articles.router import router as articles_router
from app.users.router import router as users_router

app = FastAPI()

app.include_router(users_router)
app.include_router(articles_router)
