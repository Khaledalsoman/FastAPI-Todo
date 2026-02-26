from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import FastAPI,Depends
import models
from database import engine,SessionLocal
from models import Todos
from pydantic import BaseModel

app=FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency=Annotated[Session,Depends(get_db)]

class Todo_request(BaseModel):
    title: str
    description: str
    priority: int
    complete: bool

@app.get('/')
async def read_all(db:db_dependency):
    return db.query(Todos).all()

@app.post('/')
def post_todo(db:db_dependency,todo_request:Todo_request):
    todo_model=Todos(**todo_request.dict())

    db.add(todo_model)
    db.commit()

