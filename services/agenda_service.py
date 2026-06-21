from database.agenda_db import *
from database.task_db import *

from services.activity_service import *


def create_agenda_service(user_id, judul, deskripsi, tanggal, prioritas):
    add_agenda(user_id, judul, deskripsi, tanggal, prioritas)

    log_create_agenda(user_id, judul)


def edit_agenda_service(user_id, agenda_id, judul, deskripsi, tanggal, prioritas):
    update_agenda(agenda_id, judul, deskripsi, tanggal, prioritas)

    log_edit_agenda(user_id, judul)


def delete_agenda_service(user_id, agenda_id):
    agenda = get_agenda_by_id(agenda_id)

    log_delete_agenda(user_id, agenda[2])

    delete_agenda(agenda_id)


def create_task_service(user_id, agenda_id, nama_tugas):
    add_task(agenda_id, nama_tugas)

    log_create_task(user_id, nama_tugas)


def edit_task_service(user_id, task_id, nama_tugas):
    update_task(task_id, nama_tugas)

    log_edit_task(user_id, nama_tugas)


def delete_task_service(user_id, task_id):
    task = get_task_by_id(task_id)

    log_delete_task(user_id, task[2])

    delete_task(task_id)


def change_task_status_service(user_id, task_id, status):
    task = get_task_by_id(task_id)

    update_task_status(task_id, status)

    log_change_task_status(user_id, task[2], status)

