from typing import Annotated
from fastapi import Depends, status,HTTPException
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
from data.pydantic_model_user import *

from handler.work_db import *
#library fro jwt
import secrets
from datetime import datetime, timedelta, timezone
import jwt
from jwt.exceptions import InvalidTokenError

#settings for jwt token
SECRET_KEY = secrets.token_hex(64)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

#temp test
users_db = {
    
}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

#create jwt token
def create_acces_token(data: dict,expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15) 
    to_encode.update({'exp': expire})
    encode_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encode_jwt

 
async def get_current_user(token: Annotated[str,Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        username = payload.get('sub')
        if username is None:
            raise credentials_exception
    except InvalidTokenError:
        raise credentials_exception
    user = get_user(users_db,username=username)
    if user is None:
        raise credentials_exception
    return user