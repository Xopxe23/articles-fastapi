from sqlalchemy import (Column, DateTime, ForeignKey, Integer, String, Text,
                        func)

from app.database import Base


class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey("users.id"), nullable=False)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
