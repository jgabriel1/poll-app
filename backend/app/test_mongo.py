import os

import pymongo

client = pymongo.MongoClient(os.getenv('MONGO_URL'))
db = client.test
