from app import create_app, db  # noqa: F401
from app.models import User, BTCPayClientConnector

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {
            'db': db,
            'User': User,
            'BTCPayClientConnector': BTCPayClientConnector
            }
