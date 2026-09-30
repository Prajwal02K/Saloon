"""Customer-facing pages and admin page navigation."""
from flask import Blueprint, redirect, render_template, session, url_for

import db
from config import ADMIN_SETUP_KEY
from .common import site_config

pages_bp = Blueprint("pages", __name__)


@pages_bp.get("/")
def index():
    return render_template("index.html", cfg=site_config())


@pages_bp.get("/services")
def services():
    return render_template("services.html", cfg=site_config())


@pages_bp.get("/gallery")
def gallery():
    photos = db.list_gallery()
    for photo in photos:
        photo["src"] = photo.get("src") or url_for("static", filename=f"images/{photo['filename']}")
    return render_template("gallery.html", cfg=site_config(), photos=photos)


@pages_bp.get("/booking")
def booking():
    return render_template("booking.html", cfg=site_config())


@pages_bp.get("/reviews")
def reviews_page():
    return render_template("reviews.html", cfg=site_config())


@pages_bp.get("/admin")
def admin():
    endpoint = "pages.admin_dashboard" if session.get("admin") else "pages.admin_login_page"
    return redirect(url_for(endpoint))


@pages_bp.get("/admin/login")
def admin_login_page():
    if session.get("admin"):
        return redirect(url_for("pages.admin_dashboard"))
    first_admin = db.admin_count() == 0
    return render_template(
        "admin_login.html",
        salon_name=db.get_public_settings().get("salon", ""),
        first_admin=first_admin,
        can_signup=first_admin and bool(ADMIN_SETUP_KEY),
    )


@pages_bp.get("/admin/signup")
def admin_signup_page():
    return render_template(
        "admin_signup.html",
        salon_name=db.get_public_settings().get("salon", ""),
        first_admin=db.admin_count() == 0,
        authenticated=bool(session.get("admin")),
        setup_available=bool(ADMIN_SETUP_KEY),
    )


@pages_bp.get("/admin/dashboard")
def admin_dashboard():
    if not session.get("admin"):
        return redirect(url_for("pages.admin_login_page"))
    return render_template("admin.html", cfg=site_config())