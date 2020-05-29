from fastapi import FastAPI

from .test_mongo import db

app = FastAPI()


@app.get('/')
def root():
    return {'hello': str(db)}
