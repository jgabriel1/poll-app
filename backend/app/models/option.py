from pydantic import BaseModel


class Option(BaseModel):
    text: str
    votes: int = 0
