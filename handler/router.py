from fastapi import FastAPI, APIRouter
from typing import Annotated
from ..data.pydantic_model_task import Task

router = APIRouter()

tasks = {}

@router.get('/task/{user_id}')
async def get_all_task(user_id: Annotated[int,None] = None) -> Task:
    return tasks


@router.get('/task/{user_id}/{task_id}')
async def get_task(user_id: Annotated[int,None] = None,task_id: Annotated[int,None] = None) -> Task:
    return tasks[task_id]

@router.post('/tasks/{user_id}')
async def create_task(task: Task, user_id: Annotated[int,None] = None):
    if task:
        tasks.update({'Task': task})
        return {'Create task' : True,'Task': task}
    return {'Error' : 'Task not created'}


@router.put('/tasks/{user_id}/{task_id}')
async def update_task(task: Task, user_id: Annotated[int,None] = None,task_id: Annotated[int,None] = None):
    if task_id in tasks:
        tasks.update({task_id: task})
        return tasks
    return {'task_id': 'Not found'}


@router.delete('/tasks/{user_ud}/{task_id}')
async def delete_task(user_id: Annotated[int,None] = None,task_id: Annotated[int,None] = None):
    pass
