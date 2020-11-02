from flask import Blueprint
from flask_cors import CORS

callbacks = Blueprint('callbacks', __name__)
CORS(callbacks)

from app.callbacks import routes  # noqa: F401 E402
