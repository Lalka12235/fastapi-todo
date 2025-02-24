from fastapi import APIRouter
from typing import Annotated
from data.pydantic_model_task import Task

router = APIRouter()

tasks = {}

@router.get('/tasks/{user_id}')
async def get_all_task(user_id: Annotated[str, None]):
    if user_id in tasks:
        task_temp = tasks.get(user_id)
        return task_temp
    return {'user_id' : 'Not found'}


@router.get('/tasks/{user_id}/{task_id}')
async def get_task(user_id: Annotated[str, None],task_id: Annotated[str,None]) -> Task:
    if user_id in tasks:
        task_temp = tasks.get(user_id)
        return task_temp[task_id]
    return {'user_id' : 'Not found'}

@router.post('/tasks/{user_id}')
async def create_task(task: Task, user_id: Annotated[str, None],task_id: Annotated[str,None]):
    if task:
        tasks.update({user_id: {task_id: task}})
        return {'Create task' : True,user_id: tasks[user_id]}
    return {'Error' : 'Task not created', 'Create task': False}


@router.put('/tasks/{user_id}/{task_id}')
async def update_task(task: Task, user_id: Annotated[str, None],task_id: Annotated[str,None]):
    if user_id in tasks:
        tasks.update({user_id: {task_id: task}})
        return tasks
    return {'task_id': 'Not found'}


@router.delete('/tasks/{user_id}/{task_id}')
async def delete_task(user_id: Annotated[str, None],task_id: Annotated[str,None]):
    if user_id in tasks:
        delete = tasks.get(user_id)
        del delete[task_id]
        return {'Delete task': True}
    return {'task_id': 'Not found','Delete task': False}
