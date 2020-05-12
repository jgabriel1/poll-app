from secrets import token_urlsafe
from marshmallow import fields, Schema, post_load
from app.models import Poll, Option


class CreatePollSchema(Schema):
    question = fields.String()
    allow_multiple = fields.Boolean()
    options = fields.List(fields.String())

    @post_load
    def create_models(self, item, **kwargs):
        poll = Poll(**{
            'id': token_urlsafe(4),
            'question': item['question'],
            'allow_multiple': item['allow_multiple']
        })

        options = [
            Option(**{
                'id': token_urlsafe(8),
                'text': option,
                'votes': 0,
                'poll_id': poll.id
            })
            for option in item['options']
        ]

        return poll, options


class VotePollSchema(Schema):
    ids = fields.List(fields.String())
    votes = fields.List(fields.Boolean())

    @post_load
    def create_lists(self, item, **kwargs):
        return item['ids'], item['votes']
