from pydantic import BaseModel

class Task(BaseModel): # Мейби добавить примеры 
    title: str
    description: str | None = None
    check: bool = False


class User(BaseModel):
    username: str
    password: str


class UserOut(User):
    username: str