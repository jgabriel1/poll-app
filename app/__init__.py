from flask import Flask
from .views import *
from .models import *


def create_app(config: object):
    app = Flask(__name__)
    app.app_context().push()

    # Apply configurations:
    app.config.from_object(config)

    # Bind app to external libraries:
    db.init_app(app)
    ma.init_app(app)

    db.create_all()

    app.register_blueprint(view)
    return app
