from fastapi import APIRouter, Depends, status, HTTPException
from schemas.schemas import ShowUser, UserModel
from sqlalchemy.orm import Session
from repository import user
from database import get_db


router = APIRouter(
    prefix='/user',
    tags=['Users']
)


# Create User
@router.post('/', status_code=status.HTTP_200_OK, response_model=ShowUser)
def create_User(request:UserModel, db:Session = Depends(get_db)):
    return user.create_User(request, db)

# Get User
@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=ShowUser)
def get_user(id:int, db:Session = Depends(get_db)):
    return user.get_user(id, db)