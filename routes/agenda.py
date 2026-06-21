from flask import Blueprint, render_template, request, redirect, session

from database.agenda_db import *
from database.task_db import *
from services.agenda_service import *

agenda_bp = Blueprint("agenda", __name__)


@agenda_bp.route("/create-agenda", methods=["GET", "POST"])
def create_agenda():

    if "user_id" not in session:
        return redirect("/login")

    if request.method == "POST":

        judul = request.form["judul"]
        deskripsi = request.form["deskripsi"]
        tanggal = request.form["tanggal"]

        prioritas = 0

        if "prioritas" in request.form:
            prioritas = 1

        create_agenda_service(
            session["user_id"],
            judul,
            deskripsi,
            tanggal,
            prioritas
        )

        return redirect("/dashboard")

    return render_template("agenda/create.html")


# =====================
# DETAIL AGENDA
# =====================
@agenda_bp.route("/agenda/<int:agenda_id>")
def detail_agenda(agenda_id):

    if "user_id" not in session:
        return redirect("/login")

    agenda = get_agenda_by_id(agenda_id)

    tasks = get_tasks(agenda_id)

    agenda_finished = is_agenda_finished(agenda_id)

    return render_template(
        "agenda/detail.html",
        agenda=agenda,
        tasks=tasks,
        agenda_finished=agenda_finished,
    )


@agenda_bp.route("/edit-agenda/<int:agenda_id>", methods=["GET", "POST"])
def edit_agenda(agenda_id):

    if "user_id" not in session:
        return redirect("/login")

    agenda = get_agenda_by_id(agenda_id)

    if request.method == "POST":

        judul = request.form["judul"]
        deskripsi = request.form["deskripsi"]
        tanggal = request.form["tanggal"]

        prioritas = 0

        if "prioritas" in request.form:
            prioritas = 1

        edit_agenda_service(
            session["user_id"], agenda_id, judul, deskripsi, tanggal, prioritas
        )

        return redirect("/dashboard")

    return render_template("agenda/edit.html", agenda=agenda)


@agenda_bp.route("/delete-agenda/<int:agenda_id>")
def remove_agenda(agenda_id):

    if "user_id" not in session:
        return redirect("/login")

    delete_agenda_service(session["user_id"], agenda_id)

    return redirect("/dashboard")


@agenda_bp.route("/add-task/<int:agenda_id>", methods=["POST"])
def create_task(agenda_id):

    if "user_id" not in session:
        return redirect("/login")

    nama_tugas = request.form["nama_tugas"]

    create_task_service(session["user_id"], agenda_id, nama_tugas)

    return redirect(f"/agenda/{agenda_id}")


@agenda_bp.route("/edit-task/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):

    if "user_id" not in session:
        return redirect("/login")

    task = get_task_by_id(task_id)

    if request.method == "POST":

        nama_tugas = request.form["nama_tugas"]

        edit_task_service(session["user_id"], task_id, nama_tugas)

        return redirect(f"/agenda/{task[1]}")

    return render_template("agenda/edit_task.html", task=task)


@agenda_bp.route("/delete-task/<int:task_id>")
def remove_task(task_id):

    if "user_id" not in session:
        return redirect("/login")

    task = get_task_by_id(task_id)

    agenda_id = task[1]

    delete_task_service(
        session["user_id"],
        task_id
    )

    return redirect(f"/agenda/{agenda_id}")


@agenda_bp.route("/update-task-status/<int:task_id>/<status>")
def change_task_status(task_id, status):

    if "user_id" not in session:
        return redirect("/login")

    task = get_task_by_id(task_id)

    change_task_status_service(
        session["user_id"],
        task_id,
        status
    )

    return redirect(f"/agenda/{task[1]}")
