from secrets import token_urlsafe
from flask import Blueprint, request, redirect
from sqlalchemy.exc import IntegrityError
from app.models import db, Poll, Option
from .schemas import CreatePollSchema, VotePollSchema

api = Blueprint('api', __name__)


@api.route('/create', methods=['POST'])
def submit_create_poll():
    schema = CreatePollSchema()
    new_poll, new_options = schema.load(request.get_json())

    while True:
        try:
            db.session.add(new_poll)
            db.session.add_all(new_options)
            db.session.commit()
            break
        except IntegrityError:
            new_poll.id = token_urlsafe(4)

    return redirect(f'/vote/{new_poll.id}')  # Redirect to poll page


@api.route('/vote/<id>', methods=['PUT'])
def submit_vote_poll(id: str):
    schema = VotePollSchema()
    ids, votes = schema.load(request.get_json())

    for option_id, voted in zip(ids, votes):
        if voted:
            option = Option.query.filter_by(id=option_id).first()
            option.votes = Option.votes + 1
            db.session.commit()

    return redirect(f'/result/{id}')
