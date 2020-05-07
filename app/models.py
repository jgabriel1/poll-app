from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()


class Poll(db.Model):
    __tablename__ = 'polls'

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    query = db.Column(db.String(1000), nullable=False)
    date_created = db.Column(db.DateTime)
    date_due = db.Column(db.DateTime)
    select_multiple = db.Column(db.Boolean, nullable=True, default=True)
    options = db.relationship('Option', backref='polls')


class Option(db.Model):
    __tablename__ = 'options'

    id = db.Column(db.String, primary_key=True)
    text = db.Column(db.String(1000), nullable=False)
    votes = db.Column(db.Integer)
    poll_id = db.Column(db.String, db.ForeignKey('polls.id'), nullable=False)


class PollSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Poll
        include_relationships = True
        load_instance = True


class OptionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Poll
        include_fk = True
        load_instance = True


poll_schema = PollSchema()
option_schema = OptionSchema()
options_schema = OptionSchema(many=True)
