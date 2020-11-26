from flask import Flask

def create_app() -> Flask:

    flask_app = Flask('sample_api')

    from api.controller import sample_app
    flask_app.register_blueprint(sample_app)

    return flask_app
