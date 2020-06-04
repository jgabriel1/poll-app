import os

from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.database import Database
from pymongo.client_session import ClientSession

load_dotenv()

MONGO_URL = os.getenv('MONGO_URL')
client = MongoClient(host=MONGO_URL)


def get_db() -> Database:
    db = client.poll_app
    return db


def get_session() -> ClientSession:
    session = client.start_session()
    try:
        yield session
    finally:
        session.end_session()
