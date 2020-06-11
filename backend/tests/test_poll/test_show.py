from secrets import token_urlsafe
from typing import List

import pytest
from fastapi.testclient import TestClient
from pydantic import create_model
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND


@pytest.fixture
def sample_poll() -> dict:
    return {
        'question': 'This is the test question.',
        'options': ['This is test option 1', 'This is test option 2'],
        'allow_multiple': True
    }


@pytest.fixture
def poll_url(client: TestClient, sample_poll) -> str:
    '''Creates a poll and returns the url payload.'''

    response = client.post('/poll', json=sample_poll, headers={
        'content-type': 'application/json'
    })
    assert response.status_code == HTTP_201_CREATED

    return response.json().get('url')


def test_show_poll(client: TestClient, poll_url, sample_poll):
    response = client.get(f'/poll/{poll_url}')

    assert response.status_code == HTTP_200_OK

    option_model = create_model('option', **{
        'text': (str, ...),
        'votes': (int, ...)
    })

    poll_model = create_model('poll', **{
        'question': (str, ...),
        'options': (List[option_model], ...),
        'allow_multiple': (bool, ...)
    })

    assert poll_model.validate(response.json())

    expected_poll = {
        'question': 'This is the test question.',
        'options': [
            {'text': 'This is test option 1', 'votes': 0},
            {'text': 'This is test option 2', 'votes': 0},
        ],
        'allow_multiple': True
    }

    assert response.json() == expected_poll


def test_show_inexistent_poll(client: TestClient, poll_url):
    random_url = token_urlsafe(nbytes=8)
    assert random_url != poll_url

    response = client.get(f'/poll/{random_url}')

    assert response.status_code == HTTP_404_NOT_FOUND
