# from fastapi import FastAPI
# from typing import Optional

# from pydantic import BaseModel


# app = FastAPI()

# # Home
# @app.get("/blog")
# def index(limit, published:bool = True, sort:Optional[str] = None): # limit, published, sort are query parameters
#     if published:
#         return {f"{published}" : f"{limit} {sort} Published Blogs."}
#     else:
#         return {f"{published}" : f"{limit} {sort} Unpublished Blogs."}
    
#     #return {"data" : f"{limit} blog  from DB."}


# @app.get("/blog/{topic}") # topic is path parameter
# def unpublished_blog(topic: str):
#     return {"blog" : topic}


# # fetch the blog with id = id
# @app.get("/blog/{id}")
# def show(id: int):
#     return {"blog" : id} 


# # Model Creation
# class Blog(BaseModel): 
#     id: int
#     title: str
#     description: str
#     published:Optional[bool]


# @app.post("/blog")
# def create_blog(blog: Blog): # use Blog Model
#     return {"New blog " : f"New blog created successfully! with title {blog.title}."}

