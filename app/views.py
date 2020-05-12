from flask import Blueprint, render_template, url_for
from .forms import CreateForm
from .models import db, Poll

view = Blueprint('view', __name__)


@view.route('/create', methods=['GET'])
def create_poll():
    create_form = CreateForm()
    return render_template('create.html', create_form=create_form)


@view.route('/vote/<id>', methods=['GET'])
def vote_poll(id: str):
    poll = Poll.query.filter_by(id=id).first_or_404()
    return render_template('vote.html', poll=poll)


@view.route('/result/<id>', methods=['GET', 'PUT'])
def poll_result(id: str):
    poll = Poll.query.filter_by(id=id).first_or_404()
    poll.options.sort(key=lambda option: option.votes, reverse=True)
    return render_template('result.html', poll=poll)
