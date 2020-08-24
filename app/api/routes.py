from flask import jsonify, request

from app import db
from app.api import api
from app.decorators import token_required
from app.models import BTCPayClientConnector, StreamElementsConnector, User
from sqlalchemy.orm.exc import NoResultFound

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


@api.route('/payments', methods=['GET'])
def get_payments_connector():
    data = request.args
    try:
        username = data['username']
    except KeyError:
        return jsonify({
            'success': False,
            'error': 'invalid_form'
            })
    try:
        user = User.query.filter_by(username=username).one()
    except NoResultFound:
        return jsonify({
            'success': False,
            'error': 'user_not_found'
            })
    return jsonify({
        'success': True,
        'user': user.tip_page_export()
        })
