from flask import Blueprint, render_template, url_for, request, redirect
from sqlalchemy.exc import IntegrityError
from secrets import token_urlsafe
from .forms import CreateForm, PollForm
from .models import db, Poll, poll_schema, options_schema

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

        return redirect(f'/poll/{new_poll.id}')  # Redirect to poll page

    create_form = CreateForm()
    return render_template('create.html', create_form=create_form)


@view.route('/poll/<id>', methods=['GET', 'POST'])
def vote_poll(id: str):
    # poll = True  # Poll.query.filter...first_or_404() <- use this?
    # poll_form = PollForm.from_dict(poll)
    return f'{id}'
