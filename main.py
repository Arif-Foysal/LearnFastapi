from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

@app.get("/")
def read_root():
    return {"data": "Welcome to the API"}

@app.get("/blog")
def read_blog(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {"data": f"Blog List with limit {limit} and published status {published}"}  
@app.get("/blog/{id}")
def show_blog(id: int, q: str = None):
    return {"id": id, "q": q}  


@app.get("/blog/unpublished")
def read_unpublished():
    return {"data": "Unpublished Blogs"}
# Dynamic routers after the static routes to avoid conflicts
@app.get("/blog/{id}/comments")
def read_comments(id: int):
    return {"id": id, "comments": ["Comment 1", "Comment 2"]}

class Blog(BaseModel):
    title: str
    content: str


@app.post("/blog")
def create_blog(blog: Blog):
    return {"data": f"Blog '{blog.title}' created with content: {blog.content}"}