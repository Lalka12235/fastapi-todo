from fastapi import APIRouter
from typing import Annotated
from app.data.pydantic_model_task import Task
from app.db.create_db import create_db
from app.db.work_db import get_all_task_db,get_task_db,create_task_db,update_task_db,delete_task_db

import os

router = APIRouter()
path_to_db = 'app/db/tasks.db'
#Create db
if os.path.exists(path_to_db):
    pass
else:
    tasks_db = create_db()

tasks = {}

User_id = Annotated[str, None]
Task_id = Annotated[str,None]

@router.get('/tasks/{user_id}')
async def get_all_task(user_id: User_id):
    task_temp = get_all_task_db(path_to_db,user_id)
    if task_temp:
        return task_temp
    return {'Found': False}


@router.get('/tasks/{user_id}/{task_id}')
async def get_task(user_id: User_id,task_id: Task_id):
    task_temp = get_task_db(path_to_db,user_id,task_id)
    if task_temp:
        return {
            "username": task_temp[0],
            "task_id": task_temp[1],
            "description": task_temp[3],
            "is_completed": bool(task_temp[4])
        }
    return {'user_id' : 'Not found'}

@router.post('/tasks/{user_id}')
async def create_task(task: Task, user_id: User_id,): 
    creation = create_task_db(path_to_db,user_id,task)
    return {'Create task' : True}



@router.put('/tasks/{user_id}/{task_id}')
async def update_task(task: Task, user_id: User_id,task_id: Task_id):
    task_temp = get_task_db(path_to_db,user_id,task_id)
    if task_temp:
        creation = update_task_db(path_to_db,user_id,task_id,task)
        return {'Update': True,'Task': creation}
    return {'task_id': 'Not found'}


@router.delete('/tasks/{user_id}/{task_id}')
async def delete_task(user_id: User_id,task_id: Task_id):
    delete = delete_task_db(path_to_db,user_id,task_id)
    if delete:
        return {'Delete task': True}
    return {'task_id': 'Not found','Delete task': False}
