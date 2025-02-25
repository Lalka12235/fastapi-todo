#framework
from fastapi import APIRouter, Depends, status,HTTPException
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from data.pydantic_model_user import *

#handlers
from handler.work_db import *
from handler.hash import *
from handler.generate_jwt import *


auth = APIRouter()

@auth.post('/auth/register')
async def register_account(user: UserRegister):
    find_user = get_user(users_db, user.username)
    
    if find_user:
        return {'message': 'User already exists'}

    hashed_password = make_hash_pass(user.password)
    new_user = UserDb(username=user.username,hash_pass=hashed_password)
    users_db[user.username] = new_user.dict()
    
    return UserOut(username=user.username)


@auth.post('/token/login')
async def login_for_acces_token(form_data: Annotated[OAuth2PasswordRequestForm,Depends()]) -> Token:
    user = authenticate_user(users_db,form_data.username,form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    acces_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_acces_token(
        data ={'sub': user.username},expires_delta=acces_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")

@auth.get('/users/')
async def read_users(user: Annotated[str,Depends(get_current_user)]):
    return users_db
