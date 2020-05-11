import re
from time import sleep
from tests.live_tests.setup import BaseLiveTest, PollTest
from app.models import db, Poll


class LiveTestCreate(BaseLiveTest):

    def test_create_poll(self):
        poll_test = PollTest()
        self.driver.get(f'{poll_test.url}/create')

        question, allow_multiple, options, add_button = self.find_create_nodes()

        button_presses = 0
        while len(options) < len(poll_test.options):
            add_button.click()
            button_presses += 1
            options = self.driver.find_elements_by_class_name('poll-option')

        with self.subTest('test_adding_options'):
            self.assertEqual(len(options), len(poll_test.options))
            self.assertEqual(button_presses, len(poll_test.options) - 2)

        question.send_keys(poll_test.question)

        for _input, value in zip(options, poll_test.options):
            _input.send_keys(value)

        with self.subTest('test_typed_in'):
            self.assertEqual(
                poll_test.question,
                question.get_attribute('value')
            )

            for _input, value in zip(options, poll_test.options):
                self.assertEqual(value, _input.get_attribute('value'))

        submit = self.driver.find_element_by_id('submit-poll-form')
        submit.click()
        sleep(3)

        url = self.driver.current_url
        with self.subTest('test-redirecting-to-vote'):
            regex = re.compile(r'^(http:\/\/localhost:8943\/vote\/).{6}$')
            self.assertRegex(url, regex)

        # Check database directly:
        poll_id = url.split('/')[-1]
        poll_db = Poll.query.filter_by(id=poll_id).first()
        options_db = poll_db.options

        with self.subTest('test-created-in-database'):
            self.assertTrue(poll_db)
            self.assertTrue(options_db)

            self.assertEqual(poll_db.question, poll_test.question)
            for created, intended in zip(poll_db.options, poll_test.options):
                self.assertEqual(created.text, intended)
                self.assertEqual(created.poll_id, poll_id)

        self.driver.close()
