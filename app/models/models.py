from app import db  # noqa: F401


class BTCPayClientConnector(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    client = db.Column(db.PickleType)

    user_id = db.Column(
            db.Integer, db.ForeignKey('user.id')
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
