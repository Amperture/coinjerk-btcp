from app import db
from app.models import AlertServiceNotifierClient
from app.workers import StreamElementsJWTClient


def alerts_streamelements_setup(params):
    return StreamElementsJWTClient(
            user_id=params['client_id'],
            jwt_token=params['jwt_token']
            )


alert_account_setup_switch = {
        'streamelements': alerts_streamelements_setup,
        }


def setup_alert_account(user, params):
    client = alert_account_setup_switch[params['type']](params)
    asn = user.alert_service_notifier
    print(asn)
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
