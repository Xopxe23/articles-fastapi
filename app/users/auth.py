from datetime import datetime, timedelta

from fastapi import Depends
from jose import jwt
from passlib.context import CryptContext

from app.config import settings
from app.users.dao import UserDAO

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


async def authenticate_user(email: str, password: str):
    user = await UserDAO.find_one_or_none(email=email)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user


async def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, settings.ALGORITHM)
    return encoded_jwt
