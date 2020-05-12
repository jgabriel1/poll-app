from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


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
