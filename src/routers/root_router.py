from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from src.configs.message_config import AppMessages

from src.configs.app_config import app_settings

root_router = APIRouter(prefix=app_settings.API_V1_STR)


@root_router.get(
    "/",
    status_code=status.HTTP_200_OK,
    tags=["root"],
    description="This endpoint returns a welcome message for new users of this API",
)
def welcome_user() -> JSONResponse:
    message: str = AppMessages.WELCOME_MESSAGE

    return JSONResponse(content={"message": message})
