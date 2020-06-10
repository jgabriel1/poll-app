def test_create_poll(client):
    poll = {
        'question': 'Test question.',
        'options': [
            'This is test option 1',
            'This is test option 2',
            'This is test option 3'
        ],
        'allow_multiple': True
    }

    response = client.post('/poll', json=poll, headers={
        'Content-Type': 'application/json'
    })

    assert response.status_code == 201
