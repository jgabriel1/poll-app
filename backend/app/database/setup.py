import os

from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.database import Database

load_dotenv()

MONGO_URL = os.getenv('MONGO_URL')
client = MongoClient(host=MONGO_URL)


def get_client() -> MongoClient:
    return client


def get_db() -> Database:
    db = client.poll_app
    return db
