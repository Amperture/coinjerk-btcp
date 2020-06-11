from flask import jsonify, request

from app import db
from app.api import api
from app.decorators import token_required
from app.models import BTCPayClientConnector, StreamElementsConnector

from btcpay import BTCPayClient


@api.route('/connectors/btcpay', methods=['GET'])
@token_required
def btcpay_connector_get(user):
    if not user.btcp_client_connector:
        return jsonify({
            'message': "No PayServer Found"
          }), 404
    else:
        return jsonify({
            'server_host': user.btcp_client_connector.client.host
          })


@api.route('/connectors/btcpay', methods=['POST'])
@token_required
def btcpay_connector_post(user):
    form = request.get_json()
    if not form['url'] or not form['code']:
        return jsonify({
            "Incomplete Form"
            }), 400

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
    return jsonify({
        'success': True
        })


@api.route('/connectors/streamelements', methods=['POST'])
@token_required
def streamelements_connector_post(user):
    form = request.get_json()
    if not form['channelID'] or not form['channelJWT']:
        return jsonify({
            "Incomplete Form"
            }), 400

    con = StreamElementsConnector(
            jwt=form['channelJWT'],
            channel_id=form['channelID']
            )

    db.session.add(con)
    db.session.commit()
    return jsonify({
        'success': True
        })
