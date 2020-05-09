from flask import Blueprint, render_template, url_for, request, redirect
from sqlalchemy.exc import IntegrityError
from secrets import token_urlsafe
from .forms import CreateForm, PollForm
from .models import db, Poll, Option, poll_schema, options_schema, option_schema

view = Blueprint('view', __name__)


@view.route('/', methods=['GET'])
def index():
    return render_template('base.html')


@view.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        poll = request.get_json()
        options = poll.pop('options')

        new_poll = poll_schema.load(poll, session=db.session)
        new_options = options_schema.load_id(options, new_poll.id, db.session)

        while True:
            try:
                db.session.add(new_poll)
                db.session.add_all(new_options)
                db.session.commit()
                break
            except IntegrityError:
                new_poll.id = token_urlsafe(4)

        return redirect(f'/vote/{new_poll.id}')  # Redirect to poll page

    create_form = CreateForm()
    return render_template('create.html', create_form=create_form)


@view.route('/vote/<id>', methods=['GET', 'PUT'])
def vote_poll(id: str):
    if request.method == 'PUT':
        json_response = request.get_json()
        option_ids = json_response.get('ids')
        results = json_response.get('results')

        for option_id, voted in zip(option_ids, results):
            if voted:
                option = Option.query.filter_by(id=option_id).first()
                option.votes = Option.votes + 1
                db.session.commit()

        return redirect(f'/result/{id}')

    # o6r_IQ
    poll = poll_schema.dump(
        Poll.query.filter_by(id=id).first_or_404()
    )

    options = options_schema.dump(
        Option.query.filter_by(poll_id=id).all(),
    )

    poll.update({'options': options})
    return render_template('vote.html', poll=poll)


@view.route('/result/<id>', methods=['GET', 'PUT'])
def poll_result(id: str):
    """
    Repeated code, refactor!!
    """
    poll = poll_schema.dump(
        Poll.query.filter_by(id=id).first_or_404()
    )

    options = options_schema.dump(
        Option.query.filter_by(poll_id=id).all(),
    )

    poll.update({'options': options})
    return render_template('result.html', poll=poll)
