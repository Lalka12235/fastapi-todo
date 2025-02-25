from data.pydantic_model_user import *
from handler.hash import *


#auth user if in db
def authenticate_user(db,username: str,password: str):
    user = get_user(db,username)
    if not user:
        return False
    if not verify_pass(password,user.hash_pass):
        return False
    return user

#get user from db
def get_user(db,username:str):
    if username in db:
        user_dict = db[username]
        return UserDb(**user_dict)
    return None

