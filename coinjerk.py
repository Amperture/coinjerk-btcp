from app import create_app, db  # noqa: F401
from app.models import User, BTCPayClientConnector, AlertServiceNotifierClient

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {
            'db': db,
            'User': User,
            'AlertServiceNotifierClient': AlertServiceNotifierClient,
            'BTCPayClientConnector': BTCPayClientConnector
            }
