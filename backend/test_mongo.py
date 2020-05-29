import os

import pymongo
from dotenv import load_dotenv

load_dotenv()
MONGO_URL = os.getenv('MONGO_URL')

client = pymongo.MongoClient(MONGO_URL)
db = client['poll_app']

polls = db.polls

_id = polls.insert_one({
    'question': 'Test question',
    'options': [
        {'text': 'option1', 'votes': 0},
        {'text': 'option2', 'votes': 0},
        {'text': 'option3', 'votes': 0},
    ],
    'allow_multiple': True,
}).inserted_id

print(_id)
