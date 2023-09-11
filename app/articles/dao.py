from app.articles.models import Article
from app.dao.base import BaseDAO


class ArticleDAO(BaseDAO):
    model = Article
