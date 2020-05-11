from time import sleep
from typing import Tuple, List
from flask_testing import TestCase
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement as Element

from app import create_app
from app.models import db, Poll, Option
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


class BaseLiveTest(TestCase):

    def create_app(self):
        config = TestingConfig()
        return create_app(config=config)

    def setUp(self):
        """Before every test."""
        db.create_all()

        options = webdriver.firefox.options.Options()
        options.set_headless()
        self.driver = webdriver.Firefox(options=options)

    def tearDown(self):
        """After every test."""
        self.driver.quit()

        db.session.remove()
        db.drop_all()

    def find_create_nodes(self) -> Tuple[Element, Element, List[Element], Element]:
        """
        Finds elements in the '/create' page, in order:
            1. Poll question input;
            2. Checkbox allowing or not more than one answer;
            3. List of option inputs, initially only 2;
            4. Add more options button.
        """
        return (
            self.driver.find_element_by_id('poll-question'),
            self.driver.find_element_by_id('allow-multiple'),
            self.driver.find_elements_by_class_name('poll-option'),
            self.driver.find_element_by_id('add-option')
        )

    def create_poll(self):
        poll_test = PollTest()
        self.driver.get(f'{poll_test.url}/create')

        question, allow_multiple, options, add_button = self.find_create_nodes()
        submit_button = self.driver.find_element_by_id('submit-poll-form')

        while len(options) < len(poll_test.options):
            add_button.click()
            options = self.driver.find_elements_by_class_name('poll-option')

        question.send_keys(poll_test.question)
        for _input, value in zip(options, poll_test.options):
            _input.send_keys(value)

        submit_button.click()
        sleep(3)

        poll_id = self.driver.current_url.split('/')[-1]
        return poll_id
