from fastapi import FastAPI
from typing import Annotated
from ..data.pydantic_model_task import Task

app = FastAPI()

@app.get('/task/{user_id}')
async def get_all_task(user_id: Annotated[int,None] = None) -> Task:
    pass


@app.get('/task/{user_id}/{task_id}')
async def get_task(user_id: Annotated[int,None] = None,task_id: Annotated[int,None] = None) -> Task:
    pass

@app.post('/tasks/{user_id}')
async def create_task(task: Task, user_id: Annotated[int,None] = None):
    if task:
        return {'Create task' : True,'Task': task}
    return {'Error' : 'Task not created'}


@app.put('/tasks/{user_id}/{task_id}')
async def update_task(task: Task, user_id: Annotated[int,None] = None,task_id: Annotated[int,None] = None):
    pass
