from fastapi import APIRouter, Response

from app.users.auth import get_password_hash, authenticate_user, create_access_token
from app.users.dao import UserDAO
from app.exceptions import EmailExistsException, IncorrectEmailOrPassword
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
        return IncorrectEmailOrPassword
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("Access token", access_token)
    return access_token
