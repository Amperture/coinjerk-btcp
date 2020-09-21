from app import db
import enum


class InvoiceStatus(enum.Enum):
    UNPAID = 0
    PAID = 1
    EXPIRED = 2
    NOTIFIED = 3


class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # status holds valid values "paid", "unpaid", "expired"
    status = db.Column(db.Enum(InvoiceStatus))
    invoice_unique_id = db.Column(db.String(64), nullable=False, unique=True)

    message = db.Column(db.String(255))
    email = db.Column(db.String(255))
    username = db.Column(db.String(255), default="Anonymous")

    raw_invoice = db.Column(db.String(4096), nullable=False)

    user_id = db.Column(
            db.Integer, db.ForeignKey('user.id'), nullable=False
            )

    payment_processor_id = db.Column(
            db.Integer,
            db.ForeignKey('payment_processor.id'),
            nullable=False
            )
