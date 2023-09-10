from fastapi import APIRouter, HTTPException, status

from app.users.auth import get_password_hash
from app.users.dao import UserDAO
from app.users.schemas import SUserAuth

router = APIRouter(prefix="/auth", tags=["Auth & Users"])


@router.post("/register")
async def register_user(user_data: SUserAuth):
    existing_user = await UserDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT)
    hashed_password = get_password_hash(user_data.password)
    await UserDAO.insert(email=user_data.email, hashed_password=hashed_password)
