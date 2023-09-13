import shutil

from fastapi import UploadFile, APIRouter

router = APIRouter(
    prefix="/images",
    tags=["Upload images"]
)


@router.post("/articles")
async def add_articles_images(name: int, file: UploadFile):
    with open(f"app/static/images/{name}.webp", "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)
