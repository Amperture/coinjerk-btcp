from flask import Blueprint, jsonify
from flask_cors import CORS

auth = Blueprint('auth', __name__)
CORS(auth)


@auth.route("/login", methods=['POST'])
def login():
    return jsonify({
        'logged_in': True
        })
