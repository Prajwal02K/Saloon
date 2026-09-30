"""Flask route blueprints grouped by customer and admin workflows."""
from .admin_auth import admin_auth_bp
from .admin_bookings import admin_bookings_bp
from .admin_catalog import admin_catalog_bp
from .pages import pages_bp
from .public_api import public_api_bp


def register_routes(app):
    for blueprint in (
        pages_bp,
        public_api_bp,
        admin_auth_bp,
        admin_catalog_bp,
        admin_bookings_bp,
    ):
        app.register_blueprint(blueprint)