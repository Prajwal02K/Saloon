"""Helpers shared by route blueprints."""
import functools
from datetime import datetime

from flask import jsonify, session

import db


def admin_required(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        if not session.get("admin"):
            return jsonify({"error": "Unauthorized"}), 401
        return function(*args, **kwargs)
    return wrapper


def site_config():
    config = db.get_public_settings()
    config["services"] = db.list_services()
    config.setdefault("stylists", [])
    config.setdefault("hours", {})
    config["year"] = datetime.now().year
    return config