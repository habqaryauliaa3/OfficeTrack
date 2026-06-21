from flask import Blueprint, render_template, redirect, session

from services.log_service import *

logs_bp = Blueprint("logs", __name__)


@logs_bp.route("/logs")
def logs():

    if "user_id" not in session:
        return redirect("/login")

    logs = get_logs_service(session["user_id"])

    return render_template(
        "logs/logs.html",
        logs=logs,
    )
