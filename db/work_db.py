import sqlite3 as sq
from data.pydantic_model_task import Task  


def get_task_db(db, username,task_id):
    with sq.connect(f'{db}') as con:
        cur = con.cursor()
        
        cur.execute("SELECT * FROM tasks WHERE username = ? and task_id = ? LIMIT 1", (username,task_id))
        result = cur.fetchone()  
        return result


def get_all_task_db(db, username):
    with sq.connect(f'{db}') as con:
        cur = con.cursor()
       
        cur.execute("SELECT * FROM tasks WHERE username = ?", (username,))
        results = cur.fetchall()  
        return results


def create_task_db(db, username, task: Task):
    with sq.connect(f'{db}') as con:
        cur = con.cursor()

        cur.execute(
            "INSERT INTO tasks (username,task, description, is_completed) VALUES (?, ?, ?,?)",
            (username,task.title, task.description, task.check)
        )
        con.commit() 


def update_task_db(db, username, task_id, task: Task):
    with sq.connect(f'{db}') as con:
        cur = con.cursor()
        # Обновляем задачу
        cur.execute(
            "UPDATE tasks SET description = ?, is_completed = ? WHERE username = ? AND task_id = ?",
            (task.description, task.check, username, task_id)
        )
        con.commit() 


def delete_task_db(db, username, task_id):
    with sq.connect(f'{db}') as con:
        cur = con.cursor()
        # Удаляем задачу
        cur.execute(
            "DELETE FROM tasks WHERE username = ? AND task_id = ?",
            (username, task_id)
        )
        con.commit()  