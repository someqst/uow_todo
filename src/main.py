from fastapi import FastAPI
from fastapi import Request
from src.utils.logging import logger
from fastapi.exceptions import HTTPException
from src.api.router.todo import router as todo_router


app = FastAPI(title="ToDo List")


@app.exception_handler(Exception)
async def default_exception_handler(req: Request, exc: Exception):
    logger.error(exc)
    raise HTTPException(status_code=500, detail="Internal Server Error")


app.include_router(todo_router, prefix="/api/v1", tags=["todo"])
