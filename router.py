from fastapi import APIRouter, Depends
from auth import get_current_user
from crud import getTasks,createTask,deleteTask
from models import Task,User
from database import get_session
from sqlmodel import Session

tasksRouter = APIRouter(
    prefix="/api",
    tags=["tasks"],
)

@tasksRouter.get("/me")
def get_Me(user: User = Depends(get_current_user)) -> User:
    return user

@tasksRouter.get("/tasks")
def get_Tasks(limit: int = 10, offset: int = 0, session: Session = Depends(get_session),user: User = Depends(get_current_user)) -> list[Task]:
    return getTasks(limit=limit,offset=offset,session=session,user=user)

@tasksRouter.post("/tasks")
def create_Task(task: Task, session: Session = Depends(get_session),user: User = Depends(get_current_user)) -> Task:
    return createTask(task,session=session,user=user)

@tasksRouter.delete("/tasks/{task_id}")
def delete_Task(task_id: int, session: Session = Depends(get_session),user: User = Depends(get_current_user)) -> Task:
    return deleteTask(id=task_id,session=session,user=user)
