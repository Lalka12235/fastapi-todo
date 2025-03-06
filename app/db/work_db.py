import sqlite3 as sq
from app.data.pydantic_model_task import Task  
from sqlalchemy import create_engine,select,delete,insert,update
from sqlalchemy.orm import sessionmaker,DeclarativeBase, Mapped, mapped_column
from app.config import settings
from app.data.orm_model import *

engine = create_engine(
    url='postgresql+psycopg://yourname:yourpass@localhost:5432/tasks',
    echo=True,
)
Session = sessionmaker(engine)

def get_task_db(username,task_id):
    with Session() as session:
        result = session.execute(select(TasksOrm).where(TasksOrm.username == username, TasksOrm.task_id == task_id).limit(1))
        result = result.fetchall()
        return result


def get_all_task_db(username):
    with Session() as session:
        result = session.execute(select(TasksOrm).where(TasksOrm.username == username))
        result = result.fetchall()
        return result


def create_task_db(username, task: Task):
    with Session() as session:
        result = session.execute(insert(TasksOrm).values(username=username,task=task.title,description=task.description,is_completed=task.check))
        session.commit()
        result = result.fetchall()
        return result


def update_task_db(username, task_id, task: Task):
    with Session() as session:
        result = session.execute(update(TasksOrm).where(TasksOrm.username == username, TasksOrm.task_id == task_id).values(task=task.title,description=task.description,is_completed=task.check))
        session.commit()



def delete_task_db(username, task_id):
    with Session() as session:
        result = session.execute(delete(TasksOrm).where(TasksOrm.username == username, TasksOrm.task_id == task_id))
        session.commit()