from flask import Blueprint, render_template, redirect, session

from services.log_service import *

from utils.security import login_required

logs_bp = Blueprint("logs", __name__)


@logs_bp.route("/logs")
@login_required
def logs():

    logs = get_logs_service(session["user_id"])

    return render_template(
        "logs/logs.html",
        logs=logs,
    )
