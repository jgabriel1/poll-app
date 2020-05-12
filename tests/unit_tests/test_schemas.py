from typing import List
from tests.setup import BaseTest, PollTest
from app.models import Poll, Option
from app.api.schemas import CreatePollSchema, VotePollSchema


class TestCreateSchema(BaseTest):

    input_data = {
        'question': 'Test Question. Is this a string?',
        'allow_multiple': False,
        'options': ['Option 1', 'Option 2', 'Option 3', 'Option 4']
    }

    schema = CreatePollSchema()

    def test_validate(self):
        validation_errors = self.schema.validate(self.input_data)
        self.assertDictEqual(validation_errors, {})

    def test_loading(self):
        poll, options = self.schema.load(self.input_data)
        self.assertTrue(poll)
        self.assertTrue(options)

    poll, options = schema.load(input_data)

    def test_poll_model(self):
        self.assertIsInstance(self.poll, Poll)

    def test_option_models(self):
        self.assertIsInstance(self.options, list)
        for option in self.options:
            self.assertIsInstance(option, Option)

    def test_same_poll_id(self):
        for option in self.options:
            self.assertEqual(self.poll.id, option.poll_id)


class TestVoteSchema(BaseTest):

    input_data = {
        'ids': ['testid_0', 'testid_1', 'testid_2', 'test_id3'],
        'votes': [True, True, False, False]
    }

    schema = VotePollSchema()

    def test_validate(self):
        validation_errors = self.schema.validate(self.input_data)
        self.assertDictEqual(validation_errors, {})

    def test_loading(self):
        ids, votes = self.schema.load(self.input_data)
        self.assertTrue(ids)
        self.assertTrue(votes)

    ids, votes = schema.load(input_data)

    def test_loading_ids(self):
        self.assertIsInstance(self.ids, list)
        for _id in self.ids:
            self.assertIsInstance(_id, str)

    def test_loading_votes(self):
        self.assertIsInstance(self.votes, list)
        for vote in self.votes:
            self.assertIsInstance(vote, bool)
