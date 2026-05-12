from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    AsyncSession,
    create_async_engine,
    AsyncEngine,
)

from src.configs.app_config import app_settings


engine: AsyncEngine = create_async_engine(app_settings.DB_URL)
Session: async_sessionmaker[AsyncSession] = async_sessionmaker(
    bind=engine,
    class_=AsyncEngine,
)
