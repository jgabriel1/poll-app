from secrets import token_urlsafe

import pytest
from fastapi.testclient import TestClient
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT


@pytest.fixture
def poll_url(client: TestClient) -> str:
    '''Creates a poll and returns the url payload.'''

    poll = {
        'question': 'This is the test question.',
        'options': ['This is test option 1', 'This is test option 2'],
        'allow_multiple': True
    }

    response = client.post('/poll', json=poll, headers={
        'content-type': 'application/json'
    })
    assert response.status_code == HTTP_201_CREATED

    return response.json().get('url')


def test_delete_poll(client: TestClient, poll_url):
    response = client.delete(f'/poll/{poll_url}')

    assert response.status_code == HTTP_204_NO_CONTENT
    assert not response.content


def test_delete_inexistent_poll(client: TestClient, poll_url):
    random_url = token_urlsafe(nbytes=8)
    assert random_url != poll_url

    response = client.delete(f'/poll/{random_url}')

    # Should still respond with 204 for simplicity, event though the poll does
    # not exist in the database and nothing was deleted:
    assert response.status_code == HTTP_204_NO_CONTENT
    assert not response.content
