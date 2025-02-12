from fastapi import FastAPI
from blog.database import Base, engine
from blog.routes import blogs, users,authentication


app = FastAPI()

Base.metadata.create_all(engine)


app.include_router(authentication.router)
app.include_router(users.router)
app.include_router(blogs.router)
