from sqlalchemy.orm import Session
from schemas.schemas import BlogSchema
from models.models import Blog
from fastapi import HTTPException, status

def get_blog(db: Session):
    AllBlog = db.query(Blog).all()
    return AllBlog

def create(request:BlogSchema, db:Session):
    new_blog = Blog(title = request.title, body = request.body, user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def show(id: int, db:Session):
    AllBlog = db.query(Blog).filter(Blog.id == id).first()
    if not AllBlog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Blog with id {id} is not avaialble.")
    return AllBlog

def update(id:int , request:BlogSchema, db:Session):
   AllBlog = db.query(Blog).filter(Blog.id == id)
   if not AllBlog.first():
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found.")
   AllBlog.update(request.model_dump(),synchronize_session=False)  # model_dum() instaed of dict()
   db.commit()
   return 'Updated !.'

def delete(id, db:Session):
    AllBlog = db.query(Blog).filter(Blog.id == id)
    if not AllBlog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found.")
    AllBlog.delete(synchronize_session=False)
    db.commit()
    return 'Deleted !'