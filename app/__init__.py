from flask import Flask
from .views import *
from .api import *
from .models import *
from config import Config


def create_app(config: Config) -> Flask:
    app = Flask(__name__)
    app.app_context().push()

    # Apply configurations:
    app.config.from_object(config)

    # Bind app to external libraries:
    db.init_app(app)
    db.create_all()

    app.register_blueprint(view)
    app.register_blueprint(api)
    return app
