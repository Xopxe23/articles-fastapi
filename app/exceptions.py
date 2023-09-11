from fastapi import HTTPException, status

EmailExistsException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Email exists"
)

IncorrectEmailOrPasswordException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Incorrect email or password"
)

TokenAbsentException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Miss token"
)

IncorrectTokenFormatException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Incorrect token"
)

TokenExpiredException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Token expired"
)

UserNotFoundException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="User not found"
)
