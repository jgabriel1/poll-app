from flask_testing import TestCase
from app import create_app
from app.models import db
from config import TestingConfig


class PollTest:
    url = 'http://localhost:8943'
    question = 'This is a test question.'
    options = [
        'Test answer 1',
        'Test answer 2',
        'Test answer 3',
        'Test answer 4',
        'Test answer 5',
    ]


class BaseTest(TestCase):

    def create_app(self):
        config = TestingConfig()
        return create_app(config=config)

    def setUp(self):
        """Before every test."""
        db.create_all()

    def tearDown(self):
        """After every test."""
        db.session.remove()
        db.drop_all()
