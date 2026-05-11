from fastapi import FastAPI

from src.configs.app_config import app_settings
from src.routers.root_router import root_router


def create_app() -> FastAPI:

    app = FastAPI(
        title=app_settings.APP_TITLE,
        summary=app_settings.APP_SUMMARY,
        contact={
            "name": app_settings.CONTACT_NAME,
            "email": app_settings.CONTACT_EMAIL,
        },
    )

    app.include_router(root_router)

    return app
