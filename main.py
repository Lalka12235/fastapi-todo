from fastapi import FastAPI
from handler.router import  get_all_task,get_task,create_task,update_task,delete_task

app = FastAPI()

#router init
app.include_router(get_all_task.router)
app.include_router(get_task.router)
app.include_router(create_task.router)
app.include_router(update_task.router)
app.include_router(delete_task.router)


@app.get('/home')
async def main():
    return {'message': 'hello'}