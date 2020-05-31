from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api import poll, vote

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(poll.router)
app.include_router(vote.router)
