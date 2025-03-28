from fastapi import Depends
from src.service.todo_service import ToDoService
from src.utils.unitofwork import IUnitOfWork, UnitOfWork


async def get_todo_service(uow: IUnitOfWork = Depends(UnitOfWork)):
    return ToDoService(uow)
