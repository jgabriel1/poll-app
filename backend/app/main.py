from fastapi import FastAPI

from .api import poll, vote

app = FastAPI()

app.include_router(poll.router)
app.include_router(vote.router)
