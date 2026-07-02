from flask import Blueprint, render_template, request, redirect, session

from database.auth_db import *
from services.auth_service import *

auth_bp = Blueprint("auth", __name__)

# =====================
# REGISTER
# =====================
@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        nama = request.form["nama"]
        username = request.form["username"]
        password = request.form["password"]

        success = register_service(nama, username, password)

        if success:
            return redirect("/login")

        return "Username sudah digunakan"

    return render_template("register.html")


# =====================
# LOGIN
# =====================
@auth_bp.route("/", methods=["GET", "POST"])
@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        user = login_service(username, password)

        if user:

            session["user_id"] = user["id"]
            session["nama"] = user["nama"]

            return redirect("/dashboard")

        return "Username atau password salah"

    return render_template("login.html")


# =====================
# LOGOUT
# =====================
@auth_bp.route("/logout")
def logout():

    session.clear()

    return redirect("/login")
