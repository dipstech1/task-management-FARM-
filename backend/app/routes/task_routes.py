from fastapi import APIRouter, Depends
from app.helpers.get_current_user import get_current_user

task_router = APIRouter(prefix="/task", tags=['Task'])

@task_router.get(path="/{task_id}")
def get_all_task(task_id:int,user_id = Depends(get_current_user)):
    return {
        'taskid': task_id,
        'user_id' : user_id
    }

@task_router.post("/")
def create_task():
    pass