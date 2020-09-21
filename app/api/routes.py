from flask import jsonify, request

from app import db
from app.api import api
from app.decorators import token_required
from app.models import (
        PaymentProcessor, AlertServiceNotifierClient, User, Invoice,
        InvoiceStatus
        )
from sqlalchemy.orm.exc import NoResultFound
from btcpay import BTCPayClient

import os
import json


@api.route('/payments/btcpay', methods=['GET'])
@token_required
def payment_processor_get(user):
    if not user.payment_processor:
        return jsonify({
            'message': "No Payment Processor Found"
          }), 404
    else:
        return jsonify({
            'server_host': user.payment_processor.client.host
          })


@api.route('/payments/btcpay', methods=['POST'])
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

    con = PaymentProcessor(
            client=client,
            user_id=user.id
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


@api.route('/connectors/streamelements', methods=['POST'])
@token_required
def streamelements_connector_post(user):
    form = request.get_json()
    if not form['channelID'] or not form['channelJWT']:
        return jsonify({
            "Incomplete Form"
            }), 400

    con = AlertServiceNotifierClient(
            jwt=form['channelJWT'],
            channel_id=form['channelID']
            )

    db.session.add(con)
    db.session.commit()
    return jsonify({
        'success': True
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
        payment_processor = user.payment_processor
    except NoResultFound:
        return jsonify({
            'success': False,
            'error': 'user_not_found',
            'error_display': "There was no user found with that name!"
            }), 404

    raw_invoice = payment_processor.create_invoice({
        'price': price,
        'currency': currency.upper(),
        'message': message,
        'tipper_name': tipper_name
        })

    export_invoice = process_btcpayserver_invoice_for_export(raw_invoice)

    return jsonify(export_invoice)
