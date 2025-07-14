from blog.database import Base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime


class Blog(Base):
    id= Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String, index=True)
    created_at = Column(DateTime, default=datetime)
    updated_at = Column(DateTime, default=datetime, onupdate=datetime)
    __tablename__ = "blogs"
