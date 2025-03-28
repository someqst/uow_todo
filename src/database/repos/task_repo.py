from src.database.repos.base_repo import Repository
from src.database.model import Tasks


class TaskRepository(Repository):
    model = Tasks
