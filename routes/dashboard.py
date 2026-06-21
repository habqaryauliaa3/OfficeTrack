from flask import Blueprint, render_template, redirect, session

from services.dashboard_service import *

dashboard_bp = Blueprint("dashboard", __name__)


# =====================
# DASHBOARD
# =====================
@dashboard_bp.route("/dashboard")
def dashboard():

    if "user_id" not in session:
        return redirect("/login")

    dashboard_data = get_dashboard_data(session["user_id"])

    return render_template(
        "dashboard/dashboard.html", nama=session["nama"], **dashboard_data
    )
