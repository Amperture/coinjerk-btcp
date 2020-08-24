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
            'error': 'user_not_found',
            'error_display': "There was no user found with that name!"
            }), 404
    return jsonify({
        'success': True,
        'user': user.tip_page_export()
        })


@api.route('/payments', methods=['POST'])
def get_invoice_from_payments_connector():
    return jsonify([{
        'id': 'btc',
        'name': 'Bitcoin',
        'icons': ['mdi-bitcoin', ],
        'address': 'bc1qvcjn825jd5zceml9j727a4fl6v5f8n9ssrryqe',
        'amount': {
          'value': '0.0001',
          'symbol': 'BTC',
          'display': True,
        },
        'walletLink': 'bitcoin:bc1qlf3p6ts3nph6qgewfe4uux8dn4cscte3jyvv7x?amount=0.00010234',
      },
      {
        'id': 'btclnd',
        'name': 'Bitcoin (LN)',
        'icons': ['mdi-flash-circle'],
        'address': 'lnbc102340n1p0nvzp9pp5mhgk5ujh5l2ehd2mjzkhulerv36409dhewmyr0g8yeyg0ae0fnksdp82pskjepqw3hjqctdwqszsnmjv3jhygzfgsazq2gcqzpgxqzupsp55h6v8ljcpje655l2wxs03vdva5j4lr6a6w5upm90huddvm00tupq9qy9qsqc4n4xqpp02ee8nsn8ugcekx7axth73u0wuhn2wjnp204qetcz7n8v9pgudtlfuqtyyspm6eqmfxegf5n988tzj39pnvz6n05d53uywcqgrjn2j',
        'amount': {
          'value': '0.0001',
          'symbol': 'BTC',
          'display': False,
        },
        'walletLink': 'lightning:lnbc102340n1p0nvzp9pp5mhgk5ujh5l2ehd2mjzkhulerv36409dhewmyr0g8yeyg0ae0fnksdp82pskjepqw3hjqctdwqszsnmjv3jhygzfgsazq2gcqzpgxqzupsp55h6v8ljcpje655l2wxs03vdva5j4lr6a6w5upm90huddvm00tupq9qy9qsqc4n4xqpp02ee8nsn8ugcekx7axth73u0wuhn2wjnp204qetcz7n8v9pgudtlfuqtyyspm6eqmfxegf5n988tzj39pnvz6n05d53uywcqgrjn2j',
      },
    ],)
