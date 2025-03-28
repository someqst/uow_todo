from src.utils.unitofwork import IUnitOfWork
from src.api.schema.todo import ToDoCreate, ToDoFromDB


class ToDoService:
    def __init__(self, uow: IUnitOfWork):
        self.uow = uow

    async def add_todo(self, todo: ToDoCreate) -> ToDoFromDB:
        todo_dict: dict = todo.model_dump()
        async with self.uow:
            todo_from_db = await self.uow.todo.add_one(todo_dict)
            todo_to_return = ToDoFromDB.model_validate(todo_from_db)
            await self.uow.commit()
            return todo_to_return

    async def get_todos(self) -> list[ToDoFromDB]:
        async with self.uow:
            todos = await self.uow.todo.get_all()
            return [ToDoFromDB.model_validate(todo) for todo in todos]

    async def get_todos_by_status(self, status: str) -> list[ToDoFromDB]:
        async with self.uow:
            todos = await self.uow.todo.get_all_by_status(status)
            return [ToDoFromDB.model_validate(todo) for todo in todos]

    async def get_todo(self, id: str) -> ToDoFromDB:
        async with self.uow:
            todo = await self.uow.todo.get_by_id(id)
            return ToDoFromDB.model_validate(todo)

    async def update_status_by_id(self, id: str, status: str) -> ToDoFromDB:
        async with self.uow:
            todo = await self.uow.todo.update_status_by_id(id, status)
            todo_return = ToDoFromDB.model_validate(todo)
            await self.uow.commit()
            return todo_return

    async def delete_by_id(self, id: str):
        async with self.uow:
            await self.uow.todo.delete_by_id(id)
            await self.uow.commit()
