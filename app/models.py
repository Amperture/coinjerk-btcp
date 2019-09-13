from app import app, db  # noqa: F401


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(64), unique=True)
    invoices = db.relationship(
            'Invoice',
            backref='user',
            lazy=True
            )
    '''
    TODO: client: one-to-one BTCPayClient
    TODO: integration: one-to-??? StreamElements/StreamLabs
    '''


class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # status holds valid values "paid", "unpaid", "expired"
    status = db.Column(db.Integer)
    btcpay_invoice_id = db.Column(db.String(64))

    message = db.Column(db.String(255))
    email = db.Column(db.String(255))
    username = db.Column(db.String(255))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id')


    '''
    TODO: client, many-to-one BTCPayClient
    '''


class BTCPayClientConnector(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client = db.Column(db.PickleType)

    '''
    user: one-to-one User
    '''


class StreamElementsConnector(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jwt = db.Column(db.String(1024))
    channel_id = db.Column(db.String(64))
