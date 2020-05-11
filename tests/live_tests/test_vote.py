from tests.live_tests.setup import BaseLiveTest, PollTest


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

            # Vote on created poll:

        self.driver.close()

    def test_allow_multiple(self):
        self.assertTrue(True)

    def test_not_allow_multiple(self):
        self.assertTrue(True)
