from app import app, db
from app.models import \
        BTCPayClientConnector, StreamElementsConnector, Invoice
from btcpay import BTCPayClient

from flask import jsonify, redirect

import requests


@app.route('/')
@app.route('/index')
def index():
    return "Hello, internet!"


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
    client_connector = BTCPayClientConnector(
            client=client
            )
    db.session.add(client_connector)
    db.session.commit()

    return jsonify({
        'code': pairing_code,
        'url': 'http://localhost:14142'
        })


@app.route('/thank_you/<string:btc_pay_id>')
def thank_you(btc_pay_id):
    invoice_id = btc_pay_id
    btcp_client = BTCPayClientConnector.query.get(1).client
    invoice_status = btcp_client.get_invoice(invoice_id)
    if invoice_status['status'] == 'complete':
        channel_id = StreamElementsConnector.query.get(1).channel_id
        jwt = StreamElementsConnector.query.get(1).jwt

        url = f"https://api.streamelements.com/kappa/v2/tips/{channel_id}/"

        headers = {
                    'Authorization': f"Bearer {jwt}",
                    'accept': "application/json",
                    'content-type': "application/json"
                    }

        data = {
                'user': {
                    'email': "a@a.com",
                    'username': "Amp"
                    },
                'provider': "CoinJerk",
                'message': "First Test of CoinJerk v3!",
                'amount': invoice_status['price'],
                'currency': "USD",
                'imported': True
                }
        response = requests.post(url, headers=headers, json=data)

    return jsonify(response)


@app.route('/create_invoice/<float:price>/<string:currency>')
@app.route('/create_invoice/<int:price>/<string:currency>')
def create_invoice(price, currency):
    btcp_conn = BTCPayClientConnector.query.get(1)
    invoice = btcp_conn.client.create_invoice({
        'price': price,
        'redirectUrl': 'http://localhost:5000/thank_you',
        'currency': currency
        })
    print(invoice)
    invoice_conn = Invoice(
            btcpay_invoice_id=invoice['id']
            )
    db.session.add(invoice_conn)
    db.session.commit()
    return redirect(invoice['url'])
