from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_bcrypt import Bcrypt

import os

basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()
cors = CORS()
bcrypt = Bcrypt()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    cors.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)

    from app.auth import auth
    app.register_blueprint(auth, url_prefix='/auth')

    from app.api import api
    app.register_blueprint(api, url_prefix='/api')

    from app.callbacks import callbacks
    app.register_blueprint(callbacks, url_prefix='/callbacks')

    return app


from app import models  # noqa: E402,F401
