from typing import List

from pydantic import BaseModel


class Option(BaseModel):
    text: str
    votes: int


class Poll(BaseModel):
    question: str
    options: List[Option]
    allow_multiple: bool


class PollInDB(Poll):
    url: str = None


class PollUrlPayload(BaseModel):
    url: str


class Votes(BaseModel):
    voted: List[bool]
