from src.configs.app_config import app_settings
from src.database.session_database import engine


async def create_tables() -> None:
    from src.models.todo_model import TodoModel
    from src.models.user_model import UserModel

    print("Create tables in main database...")

    async with engine.begin() as conn:
        await conn.run_sync(app_settings.BASE.metadata.drop_all)
        await conn.run_sync(app_settings.BASE.metadata.create_all)

    print("Tables created with success!")


if __name__ == "__main__":
    import asyncio

    asyncio.run(create_tables())
