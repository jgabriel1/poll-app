import os

from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.client_session import ClientSession

load_dotenv()

TEST_MONGO_URL = os.getenv('TEST_MONGO_URL')
client = MongoClient(host=TEST_MONGO_URL)


def get_test_db() -> ClientSession:
    with client.start_session() as session:
        yield session
