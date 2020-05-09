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


@view.route('/vote/<id>', methods=['GET', 'POST'])
def vote_poll(id: str):
    # o6r_IQ
    poll = poll_schema.dump(
        Poll.query.filter_by(id=id).first_or_404()
    )

    options = options_schema.dump_clean(
        Option.query.filter_by(poll_id=poll.get('id')).all(),
    )

    poll.update({'options': options})
    return render_template('vote.html', poll=poll)

    # to add 1 to the counter on submit:
    # https://stackoverflow.com/questions/2334824/how-to-increase-a-counter-in-sqlalchemy
