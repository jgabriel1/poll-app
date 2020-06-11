import pytest
from fastapi.testclient import TestClient

from app import app
from app.database.connection import get_db

from .database import client as mongo_client
from .database import get_test_db


@pytest.fixture(scope='session', autouse=True)
def override_test_db():
    app.dependency_overrides[get_db] = get_test_db


@pytest.fixture(scope='function', autouse=True)
def reset_db():
    test_db = mongo_client.get_database()
    test_db.drop_collection('polls')


@pytest.fixture(scope='session')
def client() -> TestClient:
    test_client = TestClient(app=app)
    return test_client
