from flask import jsonify, request, current_app

from app import db
from app.auth import auth
from app.models import User

from datetime import datetime, timedelta
from functools import wraps
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
        'iss': str(datetime.utcnow()),
        'exp': str(datetime.utcnow() + timedelta(minutes=30))
        }, current_app.config['SECRET_KEY'])

    return jsonify({
        'token': token.decode('UTF-8')
        })


def token_required(f):
    @wraps(f)
    def _verify(*args, **kwargs):
        auth_headers = request.headers.get('Authorization', '').split()

        invalid_req = {
                'message': 'Invalid Token. Please login or register.',
                'authenticated': False
                }

        expired_req = {
                'message': 'Expired Token. Please login or register.',
                'authenticated': False
                }

        if len(auth_headers) != 2:
            return jsonify(invalid_req), 401

        try:
            token = auth_headers[1]
            data = jwt.decode(token, current_app.config['SECRET_KEY'])
            user = User.query.get(data['sub'])
            if not user:
                raise RuntimeError('User Not Found')
            return f(user, *args, **kwargs)

        except jwt.ExpiredSignatureError:
            return jsonify(expired_req), 401

        except (jwt.InvalidTokenError, Exception) as e:
            print(e)
            return jsonify(invalid_req), 401


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
        'iss': str(datetime.utcnow()),
        'exp': str(datetime.utcnow() + timedelta(minutes=30))
        }, current_app.config['SECRET_KEY'])

    return jsonify({
        'token': token.decode('UTF-8'),
        'authenticated': True
        })
