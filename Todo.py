from fastapi import FastAPI
from pydantic import BaseModel,Field
from typing import Optional

app=FastAPI()

class Todos:
    id:int
    task:str
    description:str
    deadline:Optional[int] = None

    def __init__(self,id,task,description,deadline):
        self.id=id
        self.task=task
        self.description=description
        self.deadline=deadline

todos = [
    Todos(id=1, task="Study FastAPI", description="Read documentation and build a sample project", deadline=7),
    Todos(id=2, task="Buy groceries", description="Milk, Eggs, Bread, Fruits", deadline=2),
    Todos(id=3, task="Workout", description="30 minutes cardio and strength training", deadline=None),
    Todos(id=4, task="Complete assignment", description="Finish Python backend assignment", deadline=3),
    Todos(id=5, task="Call mom", description="Weekly check-in call", deadline=1),
    Todos(id=6, task="Clean room", description="Organize desk and wardrobe", deadline=2),
    Todos(id=7, task="Read book", description="Read 20 pages of a novel", deadline=None),
    Todos(id=8, task="Practice coding", description="Solve 5 LeetCode problems", deadline=5),
    Todos(id=9, task="Pay bills", description="Electricity and internet bills", deadline=4),
    Todos(id=10, task="Plan trip", description="Research destinations and budget", deadline=None),
    Todos(id=11, task="Update resume", description="Add latest project experience", deadline=6),
    Todos(id=12, task="Meditation", description="15 minutes mindfulness session", deadline=None),
]

class Todos_validation(BaseModel):
    id:int
    task:str =Field(max_length=30,min_length=2)
    description:str
    deadline:Optional[int] = None

@app.get('/todo')
def get_todo():
    return todos

@app.get('/todo/{getId}')
def get_id(getId:int):
    for i in range(len(todos)):
        if i==getId:
            return todos[i]