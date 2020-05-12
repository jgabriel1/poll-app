from tests.setup import BaseTest
from app.models import Poll, Option
from app.api.schemas import CreatePollSchema


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

    poll, options = schema.load(input_data)

    def test_poll_model(self):
        self.assertIsInstance(self.poll, Poll)

    def test_option_models(self):
        for option in self.options:
            self.assertIsInstance(option, Option)

    def test_same_poll_id(self):
        for option in self.options:
            self.assertEqual(self.poll.id, option.poll_id)
