from flask import jsonify, request

from app.callbacks import callbacks
from app.models import Invoice


@callbacks.route('/btcpay', methods=['POST'])
def btcpay_callback():
    form = request.get_json()
    if form['status'] == 'confirmed':
        invoice = Invoice.query.filter_by(invoice_unique_id=form['id']).one()
        alert_payload = {
                'username': invoice.username,
                'amount': invoice.fiat_amount,
                'currency': invoice.fiat_currency,
                'message': invoice.message
                }
        user = invoice.user
        user.alert_service_notifier.client.tip_alert(alert_payload)

    return jsonify({'status': 'ACK'}), 200
