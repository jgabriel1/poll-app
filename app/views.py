from flask import Blueprint, render_template, url_for

view = Blueprint('view', __name__)


@view.route('/', methods=['get'])
def index():
    return render_template('base.html')

