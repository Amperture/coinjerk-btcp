from flask import jsonify, request

from app.callbacks import callbacks
from app.models import Invoice

import json


@callbacks.route('/btcpay', methods=['POST'])
def btcpay_callback():
    form = request.get_json()
    from pprint import pprint
    pprint(form)
    if form['status'] == 'confirmed':
        invoice = Invoice.query.filter_by(invoice_unique_id=form['id']).one()
        alert_payload = {
                'username': invoice.username,
                'amount': json.loads(invoice.raw_invoice)['price'],
                'currency': json.loads(invoice.raw_invoice)['currency'],
                'message': invoice.message
                }
        user = invoice.user
        user.alert_service_notifier.client.tip_alert(alert_payload)

    return jsonify({'status': 'ACK'}), 200
