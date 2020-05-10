import re
from time import sleep
from tests.setup import BaseLiveTest, PollTest


class LiveTest(BaseLiveTest):

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
            self.assertEqual(button_presses, len(poll_test.options) - 2)
            self.assertEqual(len(options), len(poll_test.options))

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

        with self.subTest('test-redirected'):
            url = self.driver.current_url
            regex = re.compile(r'^http:\/\/localhost:8943\/vote\/\w{6}$')
            self.assertRegex(url, regex)

        self.driver.close()
