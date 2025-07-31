from blog.database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship

class Blog(Base):
    id= Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String, index=True)
    created_at = Column(DateTime, default=datetime)
    updated_at = Column(DateTime, default=datetime, onupdate=datetime)
    user_id = Column(Integer, ForeignKey('users.id'))
    # Establishing a relationship with the User model
    creator = relationship("User", back_populates="blogs")
    __tablename__ = "blogs"

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    created_at = Column(DateTime, default=datetime)
    blogs = relationship("Blog", back_populates="creator")
    __tablename__ = "users"