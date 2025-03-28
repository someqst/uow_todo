from fastapi import Depends
from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from src.service.todo_service import ToDoService
from src.api.dependencies import get_todo_service
from src.api.schema.todo import ToDoCreate, StatusEnum


router = APIRouter()


@router.post("/create", summary="Создание таски")
async def create_task(
    todo: ToDoCreate, todo_service: ToDoService = Depends(get_todo_service)
):
    if todo in await todo_service.get_todos():
        raise HTTPException(409, detail="Task already exists!")
    return await todo_service.add_todo(todo)


@router.get("/getAll", summary="Получение всех таск с фильтрацией по статусу")
async def get_tasks(
    status: StatusEnum | None = None,
    todo_service: ToDoService = Depends(get_todo_service),
):
    return await todo_service.get_todos_by_status(status)


@router.get("/{todo_id}", summary="Получение таска по id")
async def get_task_by_id(
    todo_id: str, todo_service: ToDoService = Depends(get_todo_service)
):
    task = await todo_service.get_todo(todo_id)
    if not task:
        raise HTTPException(404, "Not found")
    return task


@router.put("/{task_id}", summary="Обновление статуса таски по id")
async def update_task_by_id(
    task_id: str,
    status: StatusEnum,
    todo_service: ToDoService = Depends(get_todo_service),
):
    return await todo_service.update_status_by_id(task_id, status)


@router.delete("/{task_id}", summary="Удаление таски по id")
async def delete_task_by_id(
    task_id: str, todo_service: ToDoService = Depends(get_todo_service)
):
    await todo_service.delete_by_id(task_id)
