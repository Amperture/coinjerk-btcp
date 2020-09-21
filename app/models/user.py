from app import db, bcrypt


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True)
    display_name = db.Column(db.String(64))
    hashed_password = db.Column(db.String(64), nullable=False)

    invoices = db.relationship(
            'Invoice',
            backref='user',
            lazy=True
            )

    payment_processor = db.relationship(
            'PaymentProcessor',
            backref='user',
            lazy=True,
            uselist=False,
            )

    alert_service_notifier = db.relationship(
            'AlertServiceNotifierClient',
            backref='user',
            lazy=True,
            uselist=False,
            )

    def __repr__(self):
        return f'<User {self.username}>'

    @classmethod
    def authenticate(klass, **kwargs):
        username = kwargs.get('username')
        password = kwargs.get('password')

        if not username or not password:
            return None

        user = klass.query.filter_by(username=username).first()
        if not user or not user.check_password(password):
            return None

        return user

    def tip_page_export(self):
        if self.display_name is not None:
            display = self.display_name
        else:
            display = self.username

        exp = {
                'username': self.username,
                'display_name': display,
                }
        return exp

    def set_password(self, password):
        self.hashed_password = bcrypt.generate_password_hash(password)

    def pay_client(self):
        return self.payment_processor.client

    def hash_password(password):
        return bcrypt.generate_password_hash(password)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.hashed_password, password)
