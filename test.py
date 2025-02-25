from typing import Annotated
from data.pydantic_model_task import *
from db.work_db import get_all_task_db,get_task_db,create_task_db,update_task_db,delete_task_db



User_id = Annotated[str, None]
Task_id = Annotated[str,None]




