from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import pre_load, post_dump
from secrets import token_hex, token_urlsafe
from typing import List

db = SQLAlchemy()
ma = Marshmallow()


class Poll(db.Model):
    __tablename__ = 'polls'

    id = db.Column(db.String, primary_key=True)
    question = db.Column(db.String(1000), nullable=False)
    allow_multiple = db.Column(db.Boolean, nullable=True, default=True)
    options = db.relationship('Option', backref='polls')


class Option(db.Model):
    __tablename__ = 'options'

    id = db.Column(db.String, primary_key=True)
    text = db.Column(db.String(1000), nullable=False)
    votes = db.Column(db.Integer, nullable=True, default=0)
    poll_id = db.Column(db.String, db.ForeignKey('polls.id'), nullable=False)


class PollSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Poll
        load_instance = True

    @pre_load
    def preprocess(self, data, many, **kwargs):
        processed = data.copy()
        processed.update({'id': token_urlsafe(4)})
        return processed


class OptionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Option
        include_fk = True
        load_instance = True

    def load_id(self, data: List[dict], poll_id: str, session) -> List[Option]:
        """
        Creates the correct JSON format to be deserialized by the load
        function. Also helps with adding the poll_id value that is sent
        from the request.
        """
        return self.load(
            [
                {
                    'id': token_urlsafe(8),
                    'text': option,
                    'votes': 0,
                    'poll_id': poll_id
                }
                for option in data
            ],
            session=session
        )

    def dump_clean(self, data: List[Option]) -> List[dict]:
        """
        Removes id and poll_id from the serialized object to clean
        unnecessary information in the data being sent through json.
        """
        options = self.dump(data)

        for option in options:
            option.pop('id')
            option.pop('poll_id')

        return options


poll_schema = PollSchema()
option_schema = OptionSchema()
options_schema = OptionSchema(many=True)
