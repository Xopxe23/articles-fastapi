from sqlalchemy import select, ChunkedIteratorResult

from app.articles.models import Article
from app.articles.schemas import SArticleOutput
from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.users.models import User


class ArticleDAO(BaseDAO):
    model = Article

    @classmethod
    async def find_all(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(
                cls.model.id,
                User.email,
                cls.model.title,
                cls.model.content,
                cls.model.created_at
            ).select_from(cls.model).join(User, cls.model.user_id == User.id)
            article_tuple = await session.execute(query)
            articles = _to_user_scheme(article_tuple)
            return articles

    @classmethod
    async def find_by_id(cls, article_id: int, **filter_by):
        async with async_session_maker() as session:
            query = select(
                cls.model.id,
                User.email,
                cls.model.title,
                cls.model.content,
                cls.model.created_at
            ).select_from(cls.model).join(User, cls.model.user_id == User.id).where(cls.model.id == article_id)
            article_tuple = await session.execute(query)
            articles = _to_user_scheme(article_tuple)
            return articles[0] if articles else None


def _to_user_scheme(result: ChunkedIteratorResult) -> list[SArticleOutput]:
    articles_list = [SArticleOutput(
        id=result[0],
        author=result[1],
        title=result[2],
        content=result[3],
        created_at=result[4],
    ) for result in result.all()]
    return articles_list
