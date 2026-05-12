from fastapi import status
from fastapi.testclient import TestClient

from src.configs.app_config import app_settings
from src.configs.message_config import app_messages


def test_if_the_root_endpoint_returns_the_welcome_message(get_client) -> None:
    client: TestClient = get_client
    response = client.get(app_settings.API_V1_STR)

    assert response.json() == {"message": app_messages.WELCOME_MESSAGE}


def test_if_the_root_endpoint_returns_success_200_kok(get_client) -> None:
    client: TestClient = get_client
    response = client.get(app_settings.API_V1_STR)

    assert response.status_code == status.HTTP_200_OK
