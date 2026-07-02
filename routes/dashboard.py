from flask import Blueprint, render_template, session, request

from services.dashboard_service import *
from utils.security import login_required

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/dashboard")
@login_required
def dashboard():

    keyword = request.args.get("keyword", "").strip()

    data = get_dashboard_data(session["user_id"])

    status = request.args.get("status", "semua")

    prioritas = request.args.get("prioritas", "semua")

    if (
        keyword
        or status != "semua"
        or prioritas != "semua"
    ):

        data["daftar_agenda"] = filter_agendas_service(
            session["user_id"],
            keyword,
            status,
            prioritas
        )

    data["daftar_agenda"] = add_deadline_status(
        data["daftar_agenda"]
    )

    data["daftar_agenda"] = add_progress_data(
        data["daftar_agenda"]
    )

    return render_template(
        "dashboard/dashboard.html",
        nama=session["nama"],
        keyword=keyword,
        status=status,
        prioritas=prioritas,
        **data
    )
