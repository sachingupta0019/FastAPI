from fastapi import FastAPI
from database import Base, engine
from routes import blogs, users,authentication

app = FastAPI()

Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(users.router)
app.include_router(blogs.router)

