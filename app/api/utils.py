from app import db
from app.models import (
        AlertServiceNotifierClient, PaymentProcessor
        )
from app.workers import StreamElementsJWTClient

from btcpay import BTCPayClient


def alerts_streamelements_setup(params):
    return StreamElementsJWTClient(
            user_id=params['client_id'],
            jwt_token=params['jwt_token']
            )


def btcpay_server_setup(params):
    return BTCPayClient.create_client(
            host=params['host'],
            code=params['code']
            )


def btcpay_tor_server_setup(params):
    return BTCPayClient.create_tor_client(
            host=params['host'],
            code=params['code'],
            proxy='socks5h://127.0.0.1:9050',
            )


alert_account_setup_switch = {
        'streamelements': alerts_streamelements_setup,
        }

payment_processor_setup_switch = {
        'btcpay': btcpay_server_setup,
        'btcpay-tor': btcpay_tor_server_setup
        }


def setup_alert_account(user, params):
    client = alert_account_setup_switch[params['type']](params)
    asn = user.alert_service_notifier
    if not asn:
        new_asn = AlertServiceNotifierClient(
                client=client,
                user_id=user.id
                )
        db.session.add(new_asn)
        db.session.commit()
    else:
        asn.client = client
        db.session.commit()


def setup_payment_processor(user, params):
    client = payment_processor_setup_switch[params['type']](params)
    pp_instance = user.payment_processor
    if not pp_instance:
        new_ppc = PaymentProcessor(
                client=client,
                user_id=user.id
                )
        db.session.add(new_ppc)
        db.session.commit()
    else:
        pp_instance.client = client
        db.session.commit()
