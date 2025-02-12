from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from blog.schemas.schemas import Login
from sqlalchemy.orm import Session
from blog.models.models import User
from blog import database, auth_token
from blog.hashing import Hash

router = APIRouter(tags=['Authentication'])

@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db:Session = Depends(database.get_db)):
    user = db.query(User).filter(User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credential.")

    if not Hash.verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect Password.")

      
    access_token = auth_token.create_access_token(data={"sub": user.email})
    return {"access_token":access_token, "token_type":"bearer"}


    