import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class SArticleInput(BaseModel):
    title: str
    content: str


class SArticleUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None


class SArticleOutput(BaseModel):
    id: int
    author: EmailStr
    title: str
    content: str
    created_at: datetime.datetime
