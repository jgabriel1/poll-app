from app import create_app
from config import TestingConfig
from flask import Blueprint, request

kill_server = Blueprint('kill_server', __name__)


@kill_server.route('/kill', methods=['GET'])
def kill_process():
    request.environ.get('werkzeug.server.shutdown')()
    return 'Shutting down...'


def create_test_server():
    test_server = create_app(config=TestingConfig())
    test_server.register_blueprint(kill_server)

    return test_server


if __name__ == "__main__":
    test_server = create_test_server()
    test_server.run(port=8943)
