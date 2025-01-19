from fastapi import status, HTTPException
from schemas.schemas import ShowUser, UserModel
from models.models import User
from sqlalchemy.orm import Session
from hashing import Hash



def create_User(request:UserModel, db:Session):
    newUser = User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    return newUser


def get_user(id:int, db:Session):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with user id {id} not found.")
    return user