from flask import request, jsonify, current_app
from app.models import User
from functools import wraps
import jwt


def token_required(f):
    @wraps(f)
    def _verify(*args, **kwargs):
        auth_headers = request.headers.get('Authorization').split()

        invalid_req = {
                'message': 'Invalid Token. Please login or register.',
                'authenticated': False
                }

        expired_req = {
                'message': 'Expired Token. Please login or register.',
                'authenticated': False
                }

        if len(auth_headers) != 1:
            print("invalid_req")
            return jsonify(invalid_req), 401

        try:

            token = auth_headers[0]
            data = jwt.decode(token, current_app.config['SECRET_KEY'])
            user = User.query.get(data['sub'])
            if not user:
                raise RuntimeError('User Not Found')

            return f(user, *args, **kwargs)

        except jwt.ExpiredSignatureError:
            print("expired_sig")
            return jsonify(expired_req), 401

        except (jwt.InvalidTokenError, Exception) as e:
            print(e)
            return jsonify(invalid_req), 401

    return _verify
