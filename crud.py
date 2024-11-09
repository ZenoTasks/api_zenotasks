from sqlmodel import select
from models import Task, User
from sqlmodel import Session
from fastapi import HTTPException

def createTask(task: Task,session:Session,user:User) -> Task:
    task.user = user
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

def getTasks(offset: int,limit: int,order_by: str,order_direction: str,session:Session,user:User) -> Task:
    tasks = session.exec(select(Task).where(Task.user == user).offset(offset).limit(limit)).all()
    match order_by:
        case "date":
            if order_direction == "asc":
                tasks.sort(key=lambda x: x.created_at)
            else:
                tasks.sort(key=lambda x: x.created_at,reverse=True)
        case "checked":
            if order_direction == "asc":
                tasks.sort(key=lambda x: x.done,reverse=True)
            else:
                tasks.sort(key=lambda x: x.done)
        case "title":
            if order_direction == "asc":
                tasks.sort(key=lambda x: x.title)
            else:
                tasks.sort(key=lambda x: x.title,reverse=True)
        case _:
            tasks.sort(key=lambda x: x.id)
    return tasks

def deleteTask(id: int,session:Session,user:User) -> Task:
    task = session.get(Task, id)
    
    if task==None:
        raise HTTPException(status_code=404, detail="Task not found")

    if task.user != user:
        raise HTTPException(status_code=401, detail="You are not authorized to delete this task")
    
    session.delete(task)
    session.commit()
    return task

def updateTask(id: int,task: Task,session:Session,user:User) -> Task:
    taskDB = session.get(Task, id)
    
    if taskDB == None:
        raise HTTPException(status_code=404, detail="Task not found")

    if taskDB.user != user:
        raise HTTPException(status_code=401, detail="You are not authorized to update this task")
    
    taskDB.title = task.title
    taskDB.description = task.description
    taskDB.done = task.done
    session.add(taskDB)
    session.commit()
    session.refresh(taskDB)

    return task

def createUser(user: User,session:Session) -> User:
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def getUser(user_email: str,session:Session) -> User:
    user = session.exec(select(User).where(User.email == user_email)).first()
    return user