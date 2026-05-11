from src import create_app
from src.configs.app_config import app_settings

my_app = create_app()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app_settings.APP_LOCATION,
        host=app_settings.APP_HOST,
        port=app_settings.APP_PORT,
        reload=app_settings.APP_RELOAD,
    )
