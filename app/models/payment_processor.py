from app import db  # noqa: F401
from app.models import Invoice, InvoiceStatus, ExchangeRate

import os
import json


class PaymentProcessor(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    client = db.Column(db.PickleType, nullable=False)

    user_id = db.Column(
            db.Integer, db.ForeignKey('user.id')
            )

    invoices = db.relationship(
            'Invoice',
            backref='payment_processor',
            lazy=True,
            uselist=False,
            )

    def create_invoice(self, invoice_payload):
        fiat_currency = 'USD'
        if invoice_payload['currency'].lower() == 'btc':
            fiat_amount = ExchangeRate.query.filter_by(
                    token=fiat_currency.lower(),
                    ).one().convert_from_bitcoin(
                            invoice_payload['price']
                            )

        elif invoice_payload['currency'].lower() == 'sats':
            fiat_amount = ExchangeRate.query.filter_by(
                    token=fiat_currency.lower(),
                    ).one().convert_from_bitcoin(
                            invoice_payload['price'],
                            is_sats=True
                            )
        else:
            fiat_amount = invoice_payload['price']
            fiat_currency = invoice_payload['currency']

        raw_invoice = self.client.create_invoice({
            'price': invoice_payload['price'],
            'memo': invoice_payload['message'],
            'currency': invoice_payload['currency'],
            'notificationURL': (f'{os.getenv("FLASK_SERVER_URL")}'
                                'callbacks/btcpay')
            })

        db_invoice = Invoice(
                status=InvoiceStatus.UNPAID,
                invoice_unique_id=raw_invoice['id'],
                raw_invoice=json.dumps(raw_invoice),
                payment_processor_id=self.id,
                message=invoice_payload['message'],
                username=invoice_payload['tipper_name'],
                user_id=self.user_id,
                fiat_amount=fiat_amount,
                fiat_currency=fiat_currency,
                )

        db.session.add(db_invoice)
        db.session.commit()
        return raw_invoice
