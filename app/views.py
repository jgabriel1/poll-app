from flask import Blueprint, render_template, url_for, request
from .forms import CreateForm, PollForm

view = Blueprint('view', __name__)


@view.route('/', methods=['GET'])
def index():
    return render_template('base.html')


@view.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        # Ajax submition that will create poll in the database
        return 'POLL_CODE!'  # redirect to poll page

    create_form = CreateForm()
    return render_template('create.html', create_form=create_form)


@view.route('/poll/<id>', methods=['GET', 'POST'])
def vote_poll(id: str):
    poll = True  # Poll.query.filter...
    poll_form = PollForm.from_dict(poll)
    return f'{id}'
