import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import Generator
from urllib.parse import quote_plus
from dotenv import load_dotenv  # Load environment variables

# Load .env file
load_dotenv()

# Read environment variables
username = os.getenv("DATABASE_USER")
password = quote_plus(os.getenv("DATABASE_PASSWORD"))  # Encode special characters
host = os.getenv("DATABASE_HOST")
port = os.getenv("DATABASE_PORT")
dbname = os.getenv("DATABASE_NAME")

# Construct Database URL
SQLALCHEMY_DATABASE_URI = f"postgresql://{username}:{password}@{host}:{port}/{dbname}"

# Create engine
engine = create_engine(SQLALCHEMY_DATABASE_URI)

# Define Session and Base
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

# Dependency Injection
def get_db() -> Generator: 
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
