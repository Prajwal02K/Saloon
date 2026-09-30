"""Flask application setup and route registration."""
import os

from flask import Flask

import db
from routes import register_routes


def create_app():
    application = Flask(__name__)
    application.secret_key = os.getenv("FLASK_SECRET_KEY") or os.urandom(32)
    application.config.update(
        SESSION_COOKIE_HTTPONLY=True,
        SESSION_COOKIE_SAMESITE="Lax",
        MAX_CONTENT_LENGTH=8 * 1024 * 1024,
    )

    db.init()
    db.migrate_legacy_data()
    register_routes(application)
    return application


app = create_app()


if __name__ == "__main__":
    import os as _os
    _debug = _os.getenv("FLASK_DEBUG", "false").lower() == "true"
    app.run(host="127.0.0.1", port=int(_os.getenv("PORT", 5000)), debug=_debug)