import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGO_URL = os.getenv('MONGO_URL')
client = MongoClient(host=MONGO_URL)


def get_db():
    db = client.poll_app
    return db
