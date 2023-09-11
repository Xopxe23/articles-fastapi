from datetime import datetime

from fastapi import Depends, Request
from jose import JWTError, jwt

from app.config import settings
from app.exceptions import (IncorrectTokenFormatException,
                            TokenAbsentException, TokenExpiredException,
                            UserNotFoundException)
from app.users.dao import UserDAO


async def get_token(request: Request) -> str:
    token = request.cookies.get("access_token")
    if not token:
        raise TokenAbsentException
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        decoded_token = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
    except JWTError:
        raise IncorrectTokenFormatException
    expire = decoded_token.get("exp")
    if not expire or (int(expire) < datetime.utcnow().timestamp()):
        raise TokenExpiredException
    user_id = decoded_token.get("sub")
    if not user_id:
        raise UserNotFoundException
    user = await UserDAO.find_one_or_none(id=int(user_id))
    if not user:
        raise UserNotFoundException
    return user
