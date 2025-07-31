from pydantic import BaseModel
from datetime import datetime # Import datetime for timestamp fields

class Blog(BaseModel):
    title: str
    content: str


class ShowBlog(BaseModel):
    title: str
    content: str
    updated_at: datetime  # Use datetime for timestamp fields
    class Config:
        form_attributes = True
        # This allows the model to read data from ORM objects like SQLAlchemy models
        # and convert them to Pydantic models.

class CreateUser(BaseModel):
    username: str
    email: str
    password: str
    class Config:
        form_attributes = True  # Enable ORM mode for User model
        # This allows the model to read data from ORM objects like SQLAlchemy models
        # and convert them to Pydantic models.
class ShowUser(BaseModel):
    username: str
    email: str
    created_at: datetime
    class Config:
        form_attributes = True  # Enable ORM mode for User model
