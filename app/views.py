from flask import Blueprint, render_template, url_for, request, redirect
from sqlalchemy.exc import IntegrityError
from secrets import token_urlsafe
from .forms import CreateForm, PollForm
from .models import db, Poll, poll_schema

view = Blueprint('view', __name__)


@view.route('/', methods=['GET'])
def index():
    return render_template('base.html')


@view.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        new_poll = poll_schema.load(request.get_json())
        new_poll.id = token_urlsafe(8)

        while True:
            try:
                db.session.add(new_poll)
                db.session.commit()
                break
            except IntegrityError:
                new_poll.id = token_urlsafe(8)

        return redirect(f'/poll/{new_poll.id}')  # Redirect to poll page

    create_form = CreateForm()
    return render_template('create.html', create_form=create_form)


@view.route('/poll/<id>', methods=['GET', 'POST'])
def vote_poll(id: str):
    # poll = True  # Poll.query.filter...
    # poll_form = PollForm.from_dict(poll)
    return f'{id}'
