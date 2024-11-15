from fastapi import APIRouter, HTTPException, Depends, status
from pydantic import BaseModel
from datetime import datetime
from prisma import Prisma
from typing import Optional
from utils.db_connection import prismaDB

router = APIRouter()

class Task(BaseModel):
  description: str
  completed: Optional[bool] = False
  due: datetime | None = None

class OptionalTask(Task):
  description: Optional[str] = None
  completed: Optional[bool] = None
  due: Optional[datetime] = None


@router.get("/tasks")
async def get_tasks(db: Prisma = Depends(prismaDB)):
  tasks = await db.task.find_many()
  return { "tasks": tasks }


@router.get("/tasks/{task_id}")
async def get_task(task_id: str, db: Prisma = Depends(prismaDB)):
  task = await db.task.find_unique(where={"id": task_id})

  if task is None:
    raise HTTPException(status_code=404, detail="Task not found")
  
  return {"task": task}


@router.post("/tasks", status_code=status.HTTP_201_CREATED)
async def create_task(task_data: Task, db: Prisma = Depends(prismaDB)):
  if len(task_data.description) == 0:
    raise HTTPException(status_code=400, detail="Invalid description")
  
  task = await db.task.create({
    "description": task_data.description,
    "due": task_data.due,
    "completed": task_data.completed | False
  })

  return { "message": "Task created succesfully", "task": task }


@router.patch("/tasks/{task_id}")
async def update_task(task_id: str, task_data: OptionalTask, db: Prisma = Depends(prismaDB)):
  if not task_data:
    raise HTTPException(status_code=400, detail="No data provided for update")

  task_dict = task_data.__dict__
  fields_to_update = {key: value for key, value in task_dict.items() if value is not None}

  updated_task = await db.task.update(where={ "id": task_id}, data=fields_to_update)

  if not updated_task:
    raise HTTPException(status_code=404, detail="Task not found")


  return { "message": "Task updated succesfully", "task": updated_task }

  
@router.delete("/tasks/{task_id}")
async def delete_task(task_id, db: Prisma = Depends(prismaDB)):
  task = await db.task.delete({"id": task_id})

  if not task:
    raise HTTPException(status_code=404, detail="No task found to delete")
  
  return { "message": "Task successfully deleted", "task": task}
