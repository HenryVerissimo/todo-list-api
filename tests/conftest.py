from pytest import fixture
from typing import Iterator
from fastapi.testclient import TestClient

from src import create_app


@fixture
def get_client() -> Iterator[TestClient]:
    app = create_app()

    with TestClient(app) as client:
        yield client
