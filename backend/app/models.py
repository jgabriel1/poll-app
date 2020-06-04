from typing import List

from pydantic import BaseModel


class Option(BaseModel):
    text: str
    votes: int = 0


class Poll(BaseModel):
    question: str
    options: List[Option]
    allow_multiple: bool


class PollFromRequest(Poll):
    options: List[str]


class PollInDB(Poll):
    url: str = None

    @classmethod
    def serialize_from_request(cls, poll: PollFromRequest):
        poll.options = [
            {'text': option, 'votes': 0} for option in poll.options
        ]
        return cls.parse_obj(poll)


class PollUrlPayload(BaseModel):
    url: str


class Votes(BaseModel):
    voted: List[bool]
