from sqlalchemy import Boolean, ForeignKey, Integer, String,Column
from blog.database import Base
from sqlalchemy.orm import relationship

# Sqlalchemy Model

# Blog table
class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True,index=True)
    title = Column(String)
    body = Column(String)
    published = Column(Boolean, default=True)
    user_id = Column(Integer, ForeignKey('users.id'))

    creator = relationship("User", back_populates="blog")

# User table
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True,index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    blog = relationship("Blog", back_populates="creator")