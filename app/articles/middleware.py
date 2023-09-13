from app.exceptions import TokenAbsentException
from app.main import app
from fastapi import Request


@app.middleware("http")
async def authenticate(request: Request, call_next):
    token: str = request.cookies.get("access_token")
    if not token:
        raise TokenAbsentException
    response = await call_next(request)
    return response
