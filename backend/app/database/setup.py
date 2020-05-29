import os

from dotenv import load_dotenv
from pymongo import MongoClient


def get_db():
    load_dotenv()
    MONGO_URL = os.getenv('MONGO_URL')

    client = MongoClient(host=MONGO_URL)

    db = client.poll_app
    return db
