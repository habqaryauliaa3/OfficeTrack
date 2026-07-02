from datetime import datetime

from flask import Blueprint, render_template, request, redirect, session

from database.finance_db import *
from services.finance_service import *

from utils.security import login_required

finance_bp = Blueprint("finance", __name__)


@finance_bp.route("/finance")
@login_required
def finance():

    finance_data = get_finance_summary_service(
        session["user_id"]
    )

    bulan = request.args.get(
        "bulan",
        datetime.now().strftime("%m")
    )

    tahun = request.args.get(
        "tahun",
        datetime.now().strftime("%Y")
    )

    monthly_summary = get_monthly_summary_service(
        session["user_id"],
        bulan,
        tahun,
    )

    finance_data.update(monthly_summary)

    income_chart = get_income_chart_data_service(session["user_id"])

    expense_chart = get_expense_chart_data_service(session["user_id"])

    finance_data["income_chart"] = income_chart
    finance_data["expense_chart"] = expense_chart

    finance_data["selected_month"] = bulan
    finance_data["selected_year"] = tahun

    finance_data["income_categories"] = (
        get_income_categories()
    )

    finance_data["expense_categories"] = (
        get_expense_categories()
    )

    return render_template("finance/finance.html", **finance_data)


@finance_bp.route("/add-income", methods=["POST"])
@login_required
def create_income():

    kategori = request.form["kategori"]
    tanggal = request.form["tanggal"]
    keterangan = request.form["keterangan"]
    nominal = request.form["nominal"]

    create_income_service(session["user_id"], kategori, tanggal, keterangan, nominal)

    return redirect("/finance")


@finance_bp.route("/delete-income/<int:income_id>", methods=["POST"])
@login_required
def remove_income(income_id):



    delete_income_service(session["user_id"], income_id)

    return redirect("/finance")


@finance_bp.route("/add-expense", methods=["POST"])
@login_required
def create_expense():

    kategori = request.form["kategori"]
    tanggal = request.form["tanggal"]
    keterangan = request.form["keterangan"]
    nominal = request.form["nominal"]

    create_expense_service(
        session["user_id"],
        kategori,
        tanggal,
        keterangan,
        nominal,
    )

    return redirect("/finance")


@finance_bp.route("/delete-expense/<int:expense_id>", methods=["POST"])
@login_required
def remove_expense(expense_id):



    delete_expense_service(session["user_id"], expense_id)

    return redirect("/finance")
