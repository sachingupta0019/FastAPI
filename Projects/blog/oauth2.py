from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import auth_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


def get_current_user(data:str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Invalid or expired token",
    headers={"WWW-Authenticate": "Bearer"},
    )

    token_data = auth_token.verify_token(data, credentials_exception)

    return token_data
    