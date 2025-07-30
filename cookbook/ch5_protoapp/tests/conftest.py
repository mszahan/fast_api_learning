import pytest
from fastapi.testclient import TestClient

from protoapp.main import app


@pytest.fixture(scope='function')
def test_client():
    client = TestClient(app)
    yield client
