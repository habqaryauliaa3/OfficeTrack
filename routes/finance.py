from flask import Blueprint, render_template, request, redirect, session

from database.finance_db import *
from services.finance_service import *

finance_bp = Blueprint("finance", __name__)


@finance_bp.route("/finance")
def finance():

    if "user_id" not in session:
        return redirect("/login")

    finance_data = get_finance_summary_service(session["user_id"])

    return render_template("finance/finance.html", **finance_data)


@finance_bp.route("/add-income", methods=["POST"])
def create_income():

    if "user_id" not in session:
        return redirect("/login")

    tanggal = request.form["tanggal"]
    keterangan = request.form["keterangan"]
    nominal = request.form["nominal"]

    create_income_service(session["user_id"], tanggal, keterangan, nominal)

    return redirect("/finance")


@finance_bp.route("/delete-income/<int:income_id>")
def remove_income(income_id):

    if "user_id" not in session:
        return redirect("/login")

    delete_income_service(session["user_id"], income_id)

    return redirect("/finance")


@finance_bp.route("/add-expense", methods=["POST"])
def create_expense():

    if "user_id" not in session:
        return redirect("/login")

    tanggal = request.form["tanggal"]
    keterangan = request.form["keterangan"]
    nominal = request.form["nominal"]

    create_expense_service(
        session["user_id"],
        tanggal,
        keterangan,
        nominal,
    )

    return redirect("/finance")


@finance_bp.route("/delete-expense/<int:expense_id>")
def remove_expense(expense_id):

    if "user_id" not in session:
        return redirect("/login")

    delete_expense_service(session["user_id"], expense_id)

    return redirect("/finance")
