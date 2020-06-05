from typing import List

from pydantic import BaseModel


class PollUrlPayload(BaseModel):
    url: str


class Votes(BaseModel):
    voted: List[bool]
