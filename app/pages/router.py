from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from app.articles.router import get_all_articles
from app.articles.schemas import SArticleOutput

router = APIRouter(
    prefix="/pages",
    tags=["Frontend"]
)

templates = Jinja2Templates(directory="app/templates")


@router.get("/articles")
async def get_articles_page(
        request: Request,
        articles: list[SArticleOutput] = Depends(get_all_articles)
):
    return templates.TemplateResponse(
        name="articles.html",
        context={"request": request, "articles": articles}
    )
