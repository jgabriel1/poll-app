import os

from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.client_session import ClientSession

load_dotenv()

MONGO_URL = os.getenv('MONGO_URL')
client = MongoClient(host=MONGO_URL)


def get_db() -> ClientSession:
    with client.start_session() as session:
        yield session
