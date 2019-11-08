from flask import jsonify
from app.auth import auth


@auth.route("/login", methods=['POST'])
def login():
    return jsonify({
        'logged_in': True
        })
