from flask import jsonify, request

from app import db
from app.api import api
from app.decorators import token_required
from app.models import (
        BTCPayClientConnector, StreamElementsConnector, User, Invoice,
        InvoiceStatus
        )
from sqlalchemy.orm.exc import NoResultFound
from btcpay import BTCPayClient

import os
import requests
import json


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
        user = User.query.filter_by(username=username).one()
    except KeyError:
        return jsonify({
            'success': False,
            'error': 'invalid_form'
            }), 400
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


def extract_non_none_value_from_dict(data):
    for value in data.values():
        if value is not None:
            return value


def process_btcpayserver_invoice_for_export(invoice):

    # TODO: These need to be programmatically controlled somehow.
    CRYPTO_NAMES = {
            'BTCLike': 'Bitcoin',
            'LightningLike': 'Bitcoin (LN)'
            }
    CRYPTO_ICONS = {
            'BTCLike': ['mdi-bitcoin', ],
            'LightningLike': ['mdi-flash-circle', ],
            }
    CRYPTO_DISPLAY = {
            'BTCLike': True,
            'LightningLike': False,
            }

    export_data = []
    for crypto_info in invoice['cryptoInfo']:
        export_data.append({
            'id': crypto_info['address'],
            'name': CRYPTO_NAMES[crypto_info['paymentType']],
            'icons': CRYPTO_ICONS[crypto_info['paymentType']],
            'address': crypto_info['address'],
            'amount': {
                'value': crypto_info['totalDue'],
                'symbol': 'BTC',
                'display': CRYPTO_DISPLAY[crypto_info['paymentType']],
            },
            'walletLink': extract_non_none_value_from_dict(
                crypto_info['paymentUrls']),
            })
    return export_data


@api.route('/payments', methods=['POST'])
def get_invoice_from_payments_connector():
    form = request.get_json()
    print(form)
    message = form.get('message', '')
    tipper_name = form.get('name', 'Anonymous')
    try:
        username = form['username']
        price = form['price']
        currency = form['currency']
    except KeyError:
        return jsonify({
            'success': False,
            'error': 'invalid_form'
            }), 400
    try:
        user = User.query.filter_by(username=username).one()
        pay_client = user.pay_client()
    except NoResultFound:
        return jsonify({
            'success': False,
            'error': 'user_not_found',
            'error_display': "There was no user found with that name!"
            }), 404

    raw_invoice = pay_client.create_invoice({
        'price': price,
        'currency': currency.upper(),
        'notificationURL': (f'{os.getenv("FLASK_SERVER_URL")}'
                            'api/payments_notify')
        })

    db_invoice = Invoice(
            status=InvoiceStatus.UNPAID,
            btcpay_invoice_id=raw_invoice['id'],
            raw_invoice=json.dumps(raw_invoice),
            btcp_client_connector_id=user.btcp_client_connector.id,
            message=message,
            username=tipper_name,
            user_id=user.id,
            )

    db.session.add(db_invoice)
    db.session.commit()

    export_invoice = process_btcpayserver_invoice_for_export(raw_invoice)

    return jsonify(export_invoice)


def notify_streamelements(invoice):
    import json
    user_id = os.getenv('AMP_USER_ID')
    token = os.getenv('AMP_SE_TOKEN')

    url = f"https://api.streamelements.com/kappa/v2/tips/{user_id}/"
    headers = {
            'Authorization': f"Bearer {token}",
            'accept': "application/json",
            'content-type': "application/json"
            }
    data = {
            'user': {
                'email': "amp@amperture.com",
                'username': invoice.username
                },
            'provider': "CoinJerk",
            'message': invoice.message,
            'amount': json.loads(invoice.raw_invoice)['price'],
            'currency': json.loads(invoice.raw_invoice)['currency'],
            'imported': True
            }

    response = requests.post(url, headers=headers, json=data)
    print(response.json())


@api.route('/payments_notify', methods=['POST'])
def btcpayserver_notification():
    form = request.get_json()
    from pprint import pprint
    pprint(form)
    if form['status'] == 'confirmed':
        invoice = Invoice.query.filter_by(btcpay_invoice_id=form['id']).one()
        notify_streamelements(invoice)
    return jsonify({'status': 'ACK'}), 200
