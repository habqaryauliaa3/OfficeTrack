from database.agenda_db import *
from database.task_db import *

from services.activity_service import *


def validate_agenda(judul, tanggal):

    if not judul.strip():
        return "Judul tidak boleh kosong"

    if len(judul) > 100:
        return "Judul maksimal 100 karakter"

    if not tanggal:
        return "Tanggal wajib diisi"

    return None


def validate_task(nama_tugas):

    if not nama_tugas.strip():
        return "Nama tugas tidak boleh kosong"

    if len(nama_tugas) > 100:
        return "Nama tugas maksimal 100 karakter"

    return None


def create_agenda_service(user_id, judul, deskripsi, tanggal, prioritas):
    error = validate_agenda(judul, tanggal)

    if error:
        return error

    add_agenda(user_id, judul, deskripsi, tanggal, prioritas)

    log_create_agenda(user_id, judul)

    return None 


def edit_agenda_service(user_id, agenda_id, judul, deskripsi, tanggal, prioritas):
    error = validate_agenda(judul, tanggal)

    if error:
        return error

    update_agenda(user_id, agenda_id, judul, deskripsi, tanggal, prioritas)

    log_edit_agenda(user_id, judul)

    return None

def delete_agenda_service(user_id, agenda_id):
    agenda = get_agenda_by_id(user_id, agenda_id)

    log_delete_agenda(user_id, agenda[2])

    delete_agenda(user_id, agenda_id)


def create_task_service(user_id, agenda_id, nama_tugas):
    error = validate_task(nama_tugas)
    if error:
        return error
    
    add_task(agenda_id, nama_tugas)

    log_create_task(user_id, nama_tugas)


def edit_task_service(user_id, task_id, nama_tugas):
    error = validate_task(nama_tugas)
    if error:
        return error
    update_task(user_id, task_id, nama_tugas)

    log_edit_task(user_id, nama_tugas)


def delete_task_service(user_id, task_id):
    task = get_task_by_id(user_id, task_id)

    log_delete_task(user_id, task[2])

    delete_task(user_id, task_id)


def change_task_status_service(user_id, task_id, status):
    task = get_task_by_id(user_id, task_id)

    update_task_status(user_id, task_id, status)

    log_change_task_status(user_id, task[2], status)
