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

    db.init_app(app)
    cors.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)

    from app.auth import auth
    app.register_blueprint(auth, url_prefix='/auth')

    app.config['SQLALCHEMY_DATABASE_URI'] = (
            'sqlite:///' + os.path.join(basedir, 'app.db')
            )

    return app


from app import models  # noqa: E402,F401
