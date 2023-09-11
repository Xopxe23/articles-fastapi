from fastapi import APIRouter, Depends

from app.articles.dao import ArticleDAO
from app.articles.schemas import SArticleInput
from app.users.dependencies import get_current_user
from app.users.models import User

router = APIRouter(prefix="/articles", tags=["Articles"])


@router.post("")
async def create_article(article_data: SArticleInput, current_user: User = Depends(get_current_user)):
    await ArticleDAO.insert(user_id=current_user.id, title=article_data.title, content=article_data.content)
