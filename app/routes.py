from app import app, db
from app.models import \
        PaymentProcessor, StreamElementsConnector, Invoice
from btcpay import BTCPayClient

from flask import jsonify, redirect, render_template

import requests


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/streamelements_setup/<string:chan_id>/<string:jwt>')
def streamelements_setup(chan_id, jwt):
    se_conn = StreamElementsConnector(
            jwt=jwt,
            channel_id=chan_id
            )
    db.session.add(se_conn)
    db.session.commit()
    return "SUCCESS!"


@app.route('/client_setup/<string:pairing_code>')
def client_setup(pairing_code):
    client = BTCPayClient.create_client(
            host='http://localhost:14142',
            code=pairing_code
            )
    client_connector = PaymentProcessor(
            client=client
            )
    db.session.add(client_connector)
    db.session.commit()

    return jsonify({
        'code': pairing_code,
        'url': 'http://localhost:14142'
        })
