from app import app, db  # noqa: F401
import enum


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(64), unique=True)
    invoices = db.relationship(
            'Invoice',
            backref='user',
            lazy=True
            )
    btcp_client_connector = db.relationship(
            'BTCPayClientConnector',
            backref='user',
            lazy=True,
            uselist=False,
            )
    streamelements_connector = db.relationship(
            'StreamElementsConnector',
            backref='user',
            lazy=True,
            uselist=False,
            )


class InvoiceStatus(enum.Enum):
    UNPAID = 0
    PAID = 1
    EXPIRED = 2


class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # status holds valid values "paid", "unpaid", "expired"
    status = db.Column(db.Enum(InvoiceStatus))
    btcpay_invoice_id = db.Column(db.String(64))

    message = db.Column(db.String(255))
    email = db.Column(db.String(255))
    username = db.Column(db.String(255), default="Anonymous")

    user_id = db.Column(
            db.Integer, db.ForeignKey('user.id'), nullable=False
            )
    btcp_client_connector_id = db.Column(
            db.Integer, db.ForeignKey('user.id'), nullable=False
            )


class BTCPayClientConnector(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    client = db.Column(db.PickleType)
    user_id = db.Column(
            db.Integer, db.ForeignKey('user.id'), nullable=False
            )
    invoices = db.relationship(
            'Invoice',
            backref='btcp_client_connector',
            lazy=True,
            uselist=False,
            )


class StreamElementsConnector(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jwt = db.Column(db.String(1024))
    channel_id = db.Column(db.String(64))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
