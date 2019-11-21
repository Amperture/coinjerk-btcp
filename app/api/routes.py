from flask import jsonify, request

from app import db
from app.api import api
from app.decorators import token_required
from app.models import BTCPayClientConnector

from btcpay import BTCPayClient


@api.route('/connectors/btcpay', methods=['POST'])
@token_required
def btcpay_connector_post(user):
    form = request.get_json()
    if not form['url'] or not form['code']:
        return jsonify({
            "Incomplete Form"
            }), 400

    print("URL: " + form['url'])
    print("CODE: " + form['code'])
    client = BTCPayClient.create_client(
            host=form['url'],
            code=form['code']
            )

    con = BTCPayClientConnector(
            client=client,
            user_id=user.id
            )
    db.session.add(con)
    db.session.commit()
