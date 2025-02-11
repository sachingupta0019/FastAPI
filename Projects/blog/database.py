from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import Generator

# Defining the engine
SQLALCHEMY_DATABASE_URI = "sqlite:///./blogs.db"

engine = create_engine(SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False})

# Defining the Session
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit = False,)

# Defining Base
Base = declarative_base()

# Dependency Injection
def get_db() -> Generator: 
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
