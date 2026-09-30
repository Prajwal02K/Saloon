"""Admin booking management endpoints."""
from flask import Blueprint, jsonify, request

import db
from .common import admin_required

admin_bookings_bp = Blueprint("admin_bookings", __name__)


@admin_bookings_bp.get("/api/admin/bookings")
@admin_required
def admin_bookings():
    return jsonify({"bookings": db.list_bookings(), "stats": db.stats()})


@admin_bookings_bp.patch("/api/admin/bookings/<booking_id>/status")
@admin_required
def admin_status(booking_id):
    status = request.get_json(force=True).get("status", "")
    return jsonify({"ok": db.update_booking_status(booking_id, status)})


@admin_bookings_bp.delete("/api/admin/bookings/<booking_id>")
@admin_required
def admin_delete(booking_id):
    return jsonify({"ok": db.delete_booking(booking_id)})