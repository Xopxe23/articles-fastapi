from fastapi import APIRouter, Depends, Response

from app.exceptions import (EmailExistsException,
                            IncorrectEmailOrPasswordException)
from app.users.auth import (authenticate_user, create_access_token,
                            get_password_hash)
from app.users.dao import UserDAO
from app.users.dependencies import get_current_user
from app.users.models import User
from app.users.schemas import SUserAuth

router = APIRouter(prefix="/auth", tags=["Auth & Users"])


@router.post("/register")
async def register_user(user_data: SUserAuth):
    existing_user = await UserDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise EmailExistsException
    hashed_password = get_password_hash(user_data.password)
    await UserDAO.insert(email=user_data.email, hashed_password=hashed_password)


@router.post("/login")
async def login_user(response: Response, user_data: SUserAuth):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise IncorrectEmailOrPasswordException
    access_token = await create_access_token({"sub": str(user.id)})
    response.set_cookie("access_token", access_token)
    return access_token


@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie("access_token")


@router.get("/me")
async def about_user(current_user: User = Depends(get_current_user)):
    return current_user
