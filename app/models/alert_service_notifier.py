from app import db  # noqa: F401


class AlertServiceNotifierClient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client = db.Column(db.PickleType)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
