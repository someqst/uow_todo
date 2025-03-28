from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from src.core.config import settings


engine = create_async_engine(settings.DB_URI.get_secret_value())
LocalSession = async_sessionmaker(bind=engine)
