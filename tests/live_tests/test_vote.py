import time
import random
from tests.setup import PollTest
from tests.live_tests.setup import BaseLiveTest


class LiveTestVote(BaseLiveTest):

    def test_vote_poll(self):
        # Create poll:
        poll_test = PollTest()
        poll_id = self.create_poll()

        with self.subTest('test-in-voting-page'):
            current_url = self.driver.current_url
            intended_url = f'{poll_test.url}/vote/{poll_id}'
            self.assertEqual(current_url, intended_url)

        # In voting page:
        question_text = self.driver.find_element_by_id('poll-question')
        option_checks = self.driver.find_elements_by_class_name('option-vote')
        option_labels = self.driver.find_elements_by_tag_name('label')

        with self.subTest('test-elements-are-correct'):
            self.assertEqual(poll_test.question, question_text.text)
            self.assertEqual(len(option_checks), len(option_labels))

            for checkbox, label in zip(option_checks, option_labels):
                self.assertEqual(
                    checkbox.get_attribute('id'),
                    label.get_attribute('for')
                )

            for label, intended in zip(option_labels, poll_test.options):
                self.assertEqual(label.text, intended)

        # Vote on last option of created poll:
        chosen = random.randrange(len(option_checks))
        chosen_option, chosen_label = option_checks[chosen], option_labels[chosen]

        # Chosen label element will be lost when the page changes. The text
        # needs to be stored in it's own variable:
        chosen_label_text = chosen_label.text

        # Checkbox not clickable because of bootstrap. Need to click label.
        chosen_label.click()

        submit_button = self.driver.find_element_by_id('submit-votes')
        submit_button.click()
        time.sleep(2)

        with self.subTest('test-redirected-to-results'):
            current_url = self.driver.current_url
            intended_url = f'{poll_test.url}/result/{poll_id}'
            self.assertEqual(current_url, intended_url)

        with self.subTest('test-if-vote-was-computed'):
            option_texts, option_results = (
                self.driver.find_elements_by_class_name('option-text'),
                self.driver.find_elements_by_class_name('option-result')
            )

            for option, result in zip(option_texts, option_results):
                if result.text == '1':
                    self.assertEqual(option.text, chosen_label_text)

        self.driver.close()

    def click_all_labels(self, multiple=False):
        # Create poll:
        poll_test = PollTest()
        poll_id = self.create_poll(multiple_answers=multiple)

        # In vote page:
        option_labels = self.driver.find_elements_by_tag_name('label')
        for label in option_labels:
            label.click()

        submit_button = self.driver.find_element_by_id('submit-votes')
        submit_button.click()
        time.sleep(2)
        return

    def test_allow_multiple(self):
        # In results page:
        self.click_all_labels(True)
        results = self.driver.find_elements_by_class_name('option-result')

        total_votes = sum(int(result.text) for result in results)
        self.assertGreater(total_votes, 1)

    def test_not_allow_multiple(self):
        # In results page:
        self.click_all_labels(False)
        results = self.driver.find_elements_by_class_name('option-result')

        total_votes = sum(int(result.text) for result in results)
        self.assertEqual(total_votes, 1)
