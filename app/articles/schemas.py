from pydantic import BaseModel


class SArticleInput(BaseModel):
    title: str
    content: str
