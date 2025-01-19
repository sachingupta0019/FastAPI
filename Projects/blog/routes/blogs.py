from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from schemas.schemas import ShowBlog, BlogSchema
from models.models import Blog
from sqlalchemy.orm import Session 
from database import get_db
from repository import blog

router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)


# Get All blog
@router.get('/', response_model=List[ShowBlog])
def get_all_blog(db:Session = Depends(get_db)):
    return blog.get_blog(db)

# Create a Post
@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request:BlogSchema, db:Session = Depends(get_db)):
    return blog.create(request, db)

# Show Blog with id
@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=ShowBlog)
def show(id, db:Session = Depends(get_db)):
    return blog.show(id, db)

# update
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id:int , request:BlogSchema, db:Session = Depends(get_db)):
   return blog.update(id, request, db)

# delete
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id, db:Session = Depends(get_db)):
    return blog.delete(id, db)
