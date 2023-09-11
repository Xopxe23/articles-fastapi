from fastapi import HTTPException, status

EmailExistsException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Email exists"
)

IncorrectEmailOrPassword = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Incorrect email or password"
)
