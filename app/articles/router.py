from fastapi import APIRouter, Depends

from app.articles.dao import ArticleDAO
from app.articles.schemas import SArticleInput, SArticleOutput, SArticleUpdate
from app.exceptions import PermissionDeniedException
from app.users.dependencies import get_current_user
from app.users.models import User

router = APIRouter(prefix="/articles", tags=["Articles"])


@router.post("")
async def create_article(article_data: SArticleInput, current_user: User = Depends(get_current_user)):
    await ArticleDAO.insert(user_id=current_user.id, title=article_data.title, content=article_data.content)


@router.get("", response_model=list[SArticleOutput])
async def get_all_articles():
    return await ArticleDAO.find_all()


@router.get("/{article_id}")
async def get_article_by_id(article_id: int):
    return await ArticleDAO.find_by_id(article_id)


@router.put("/{article_id}")
async def update_article(article_id: int, data: SArticleUpdate, user: User = Depends(get_current_user)):
    is_author = await ArticleDAO.find_one_or_none(user_id=user.id, id=article_id)
    if not is_author:
        raise PermissionDeniedException
    articles_data = SArticleUpdate.model_dump(data, exclude_none=True)
    return await ArticleDAO.update(article_id, articles_data)


@router.delete("/{article_id}")
async def delete_article(article_id: int, user: User = Depends(get_current_user)):
    is_author = await ArticleDAO.find_one_or_none(user_id=user.id, id=article_id)
    if not is_author:
        raise PermissionDeniedException
    return await ArticleDAO.delete(article_id)
