import pytest
from fastapi.testclient import TestClient

from api.app import app


@pytest.fixture
def api_client():
    test_client = TestClient(app)

    return test_client
