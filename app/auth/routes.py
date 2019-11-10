from flask import jsonify, request

from models import User

from app import db
from app.auth import auth


@auth.route("/login", methods=['POST'])
def login():
    return jsonify({
        'logged_in': True
        })


@auth.route("/register", methods=['POST'])
def register():
    form = request.form
    user = User(
            username=form.username,
            password=form.password
            )
    db.session.app(user)
    db.session.commit()

    return jsonify({
        'true': 'true'
        })
