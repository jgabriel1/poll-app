import time
from typing import Tuple, List
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement as Element
from tests.setup import BaseTest, PollTest


class BaseLiveTest(BaseTest):

    def setUp(self):
        super().setUp()

        options = webdriver.firefox.options.Options()
        options.set_headless()
        self.driver = webdriver.Firefox(options=options)

    def tearDown(self):
        self.driver.quit()

        super().tearDown()

    def find_elements_create(self) -> Tuple[Element, Element, List[Element], Element]:
        """
        Finds elements in the '/create' page, in order:
            1. Poll question input;
            2. Checkbox allowing or not more than one answer;
            3. List of option inputs, initially only 2;
            4. Add more options button.
        """
        return (
            self.driver.find_element_by_id('poll-question'),
            self.driver.find_element_by_xpath(
                """//label[@for="allow-multiple"]"""
            ),
            self.driver.find_elements_by_class_name('poll-option'),
            self.driver.find_element_by_id('add-option')
        )

    def create_poll(self, multiple_answers=False) -> str:
        poll_test = PollTest()
        self.driver.get(f'{poll_test.url}/create')

        question, allow_multiple, options, add_button = self.find_elements_create()
        submit_button = self.driver.find_element_by_id('submit-poll-form')

        # Get the correct amount of needed option spaces:
        while len(options) < len(poll_test.options):
            add_button.click()
            options = self.driver.find_elements_by_class_name('poll-option')

        # Type values in:
        question.send_keys(poll_test.question)
        for _input, value in zip(options, poll_test.options):
            _input.send_keys(value)

        if multiple_answers:
            allow_multiple.click()

        submit_button.click()
        time.sleep(2)

        poll_id = self.driver.current_url.split('/')[-1]
        return poll_id
