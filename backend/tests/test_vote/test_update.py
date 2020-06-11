from secrets import token_urlsafe
from typing import Callable

import pytest
from fastapi.testclient import TestClient
from starlette.status import (
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_404_NOT_FOUND,
    HTTP_406_NOT_ACCEPTABLE
)


@pytest.fixture
def create_poll(client: TestClient) -> Callable[[bool], str]:

    def poll_url(allow_multiple: bool = True) -> str:
        poll = {
            'question': 'This is the test question.',
            'options': ['This is test option 1', 'This is test option 2'],
            'allow_multiple': allow_multiple
        }

        response = client.post('/poll', json=poll, headers={
            'content-type': 'application/json'
        })
        assert response.status_code == HTTP_201_CREATED

        return response.json().get('url')

    return poll_url


def test_vote_on_poll(client: TestClient, create_poll):
    poll_url = create_poll()

    votes = {
        'voted': [True, False]
    }

    response = client.post(f'/vote/{poll_url}', json=votes)

    assert response.status_code == HTTP_204_NO_CONTENT
    assert not response.content


def test_multiple_votes_allowed(client: TestClient, create_poll):
    poll_url = create_poll(allow_multiple=True)

    votes = {
        'voted': [True, True]
    }

    response = client.post(f'/vote/{poll_url}', json=votes)

    assert response.status_code == HTTP_204_NO_CONTENT
    assert not response.content


def test_multiple_votes_not_allowed(client: TestClient, create_poll):
    poll_url = create_poll(allow_multiple=False)

    votes = {
        'voted': [True, True]
    }

    response = client.post(f'/vote/{poll_url}', json=votes)

    assert response.status_code == HTTP_406_NOT_ACCEPTABLE


def test_vote_inexistent_poll(client: TestClient, create_poll):
    poll_url = create_poll()
    random_url = token_urlsafe(nbytes=8)

    assert poll_url != random_url

    votes = {
        'voted': [True, False]
    }

    response = client.post(f'/votes/{random_url}', json=votes)

    assert response.status_code == HTTP_404_NOT_FOUND
