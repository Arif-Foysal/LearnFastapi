from fastapi import FastAPI
from pydantic import BaseModel
from . import schemas

app = FastAPI()



@app.post("/blog")
def create_blog(request: schemas.Blog):
    # Here you would typically save the blog to a database
    # For this example, we will just return the data back
    return {"data": f"Blog '{request.title}' created with content: {request.content}"}

