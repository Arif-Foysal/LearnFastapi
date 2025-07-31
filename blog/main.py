from fastapi import FastAPI, Depends,Response, status, HTTPException
from pydantic import BaseModel
from blog import schemas, models, hashing
from blog.database import engine, SessionLocal
from sqlalchemy.orm import Session
from datetime import datetime
from typing import List



app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/blog", status_code=status.HTTP_201_CREATED, tags=["Blog"])
# Create a new blog post
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    # Here you would typically save the blog to a database
    new_blog = models.Blog(title=request.title, content=request.content, created_at=datetime.now(), updated_at=datetime.now())
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    # Return the created blog or any other response as needed
    return new_blog

@app.get("/blog", status_code=status.HTTP_200_OK, response_model=List[schemas.ShowBlog],  tags=["Blog"])
def read_blog(limit: int = 10, db: Session = Depends(get_db)):
    # Here you would typically query the database for blogs
    blogs = db.query(models.Blog).limit(limit).all()
    num_blogs = db.query(models.Blog).count()
    return blogs
    
@app.get("/blog/{id}", status_code=200, response_model=schemas.ShowBlog, tags=["Blog"])
def show_blog(id: int, db: Session = Depends(get_db)):
    # Getting a specific blog by ID
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if blog:
        return blog
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found"
        )
        
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"error": "Blog not found"}

@app.put("/blog/{id}", status_code=status.HTTP_200_OK, tags=["Blog"])
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    # Updating a blog by ID
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if blog:
        blog.title = request.title
        blog.content = request.content
        blog.updated_at = datetime.now()
        db.commit()
        db.refresh(blog)
        return {"data": blog}
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found"
        )


@app.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Blog"])
def delete_blog(id: int, db: Session = Depends(get_db)):
    # Deleting a blog by ID
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if blog:
        db.delete(blog)
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found"
        )



@app.post("/user", status_code=201, response_model=schemas.ShowUser, tags=["User"])
def create_user(request: schemas.CreateUser, db: Session = Depends(get_db)):
    # Check if the username already exists
    existing_user = db.query(models.User).filter(models.User.username == request.username).first()
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail=f"Username '{request.username}' is already taken."
        )
    
    # Check if the email already exists
    existing_email = db.query(models.User).filter(models.User.email == request.email).first()
    if existing_email:
        raise HTTPException(
            status_code=400,
            detail=f"Email '{request.email}' is already registered."
        )


    # Create the new user
    new_user = models.User(
        username=request.username,
        email=request.email,
        password=hashing.bcrypt(request.password),
        created_at=datetime.now()
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get("/user/{id}", status_code=200, response_model=schemas.ShowUser, tags=["User"])
def get_user(id: int, db: Session = Depends(get_db)):
    # Retrieve a user by ID
    user = db.query(models.User).filter(models.User.id == id).first()
    if user:
        return user
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {id} not found"
        )
    