from pydantic import BaseModel
from typing import Optional, List

# Pydantic Model.

class Login(BaseModel):
    username:str
    password:str


class BlogSchema(BaseModel):
    title:str
    body:str
    published: Optional[bool]=True

    class Config():
        from_attributes = True


class UserModel(BaseModel):
    name:str
    email:str
    password:str

class ShowUser(BaseModel):
    name:str
    email:str
    blogs: List[BlogSchema] = []
    class Config():
        from_attributes = True

class ShowBlog(BaseModel):
    title:str
    body:str
    creator: ShowUser

    class Config():
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None