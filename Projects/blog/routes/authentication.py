from fastapi import APIRouter, Depends, HTTPException, status
from schemas.schemas import Login
from sqlalchemy.orm import Session
from models.models import User
import database

router = APIRouter(
    tags=['Authentication']
)

@router.post('/login')
def user_login(request: Login, db:Session = Depends(database.get_db)):
    user = db.query(User).filter(User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credential.")
    return user