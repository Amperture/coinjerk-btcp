from flask import jsonify, request, current_app

from app import db
from app.auth import auth
from app.models import User

from datetime import datetime, timedelta
import jwt


@auth.route("/login", methods=['POST'])
def login():
    data = request.get_json()
    user = User.authenticate(**data)

    if not user:
        return jsonify({
            'message': "Invalid Credentials",
            'authenticated': False
            }), 401

    token = jwt.encode({
        'sub': user.id,
        'iat': datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(minutes=30)
        }, current_app.config['SECRET_KEY'])

    return jsonify({
        'token': token.decode('UTF-8')
        })


@auth.route("/register", methods=['POST'])
def register():
    form = request.get_json()

    user = User.query.filter_by(username=form['username']).first()
    if user:
        return jsonify({
            'message': "Username Unavailable",
            'authenticated': False
            }), 400
    else:
        user = User(username=form['username'])
        user.set_password(form['password'])
        db.session.add(user)
        db.session.commit()

    token = jwt.encode({
        'sub': user.id,
        'iat': datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(minutes=30)
        }, current_app.config['SECRET_KEY'])

    return jsonify({
        'token': token.decode('UTF-8'),
        'authenticated': True
        })
