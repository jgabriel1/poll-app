import pytest
from fastapi.testclient import TestClient
from pydantic import create_model
from starlette.status import HTTP_201_CREATED, HTTP_422_UNPROCESSABLE_ENTITY


@pytest.fixture
def sample_poll() -> dict:
    return {
        'question': 'Test question.',
        'options': [
            'This is test option 1',
            'This is test option 2',
            'This is test option 3'
        ],
        'allow_multiple': True
    }


def test_create_poll(client: TestClient, sample_poll):
    response = client.post('/poll', json=sample_poll, headers={
        'Content-Type': 'application/json'
    })

    assert response.status_code == HTTP_201_CREATED

    response_model = create_model('poll_created_response', url=(str, ...))
    assert response_model.validate(response.json())


def test_create_wrong_body_schema(client: TestClient, sample_poll):
    response = client.post('/poll', json={'wrong': 'body'}, headers={
        'Content-Type': 'application/json'
    })

    assert response.status_code == HTTP_422_UNPROCESSABLE_ENTITY
