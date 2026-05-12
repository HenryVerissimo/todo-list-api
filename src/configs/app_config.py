from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    APP_TITLE: str = "Todo List API"
    APP_SUMMARY: str = "Organize your tasks with this API. Here you can create, select, update and delete your tasks through the endpoints."
    APP_VERSION: str = "0.1.0"

    API_V1_STR: str = "/api/v1"

    CONTACT_NAME: str = "Henrique Verissimo"
    CONTACT_EMAIL: str = "henriqueverissimocontato@gmail.com"

    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    APP_RELOAD: bool = True
    APP_LOCATION: str = "main:my_app"

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


app_settings = AppSettings()
