# services/dashboard_service.py
from datetime import datetime

from database.agenda_db import *
from database.task_db import is_agenda_finished, get_tasks

def get_dashboard_data(user_id):

    daftar_agenda = get_agendas(user_id)

    agenda_aktif = count_active_agendas(user_id)

    agenda_selesai = count_finished_agendas(user_id)

    return {
        "daftar_agenda": daftar_agenda,
        "agenda_aktif": agenda_aktif,
        "agenda_selesai": agenda_selesai,
    }


def search_agendas_service(user_id, keyword):

    return search_agendas(user_id, keyword)


def get_active_agendas_service(user_id):

    return get_active_agendas(user_id)


def get_finished_agendas_service(user_id):

    return get_finished_agendas(user_id)


def filter_agendas_service(user_id, keyword, status, prioritas):

    return filter_agendas(user_id, keyword, status, prioritas)


def get_deadline_status(agenda):

    agenda_id = agenda[0]
    tanggal_agenda = agenda[4]

    # Cek apakah semua task sudah selesai
    if is_agenda_finished(agenda_id):
        return "selesai"

    # Ambil tanggal hari ini
    today = datetime.today().date()

    # Ubah tanggal agenda menjadi objek date
    agenda_date = datetime.strptime(tanggal_agenda, "%Y-%m-%d").date()

    # Hitung selisih hari
    selisih_hari = (agenda_date - today).days

    if selisih_hari < 0:
        return "pending"

    elif selisih_hari == 0:
        return "hari_ini"

    elif selisih_hari == 1:
        return "h1"

    elif selisih_hari == 2:
        return "h2"

    elif selisih_hari == 3:
        return "h3"

    else:
        return "belum"


def add_deadline_status(agendas):

    hasil = []

    for agenda in agendas:

        deadline_status = get_deadline_status(agenda)

        hasil.append(
            {
                "agenda": agenda,
                "deadline_status": deadline_status,
            }
        )

    return hasil


def get_agenda_progress(agenda_id):

    tasks = get_tasks(agenda_id)

    total_task = len(tasks)

    if total_task == 0:
        return 0

    task_selesai = 0

    for task in tasks:

        if task[3] == "selesai":
            task_selesai += 1

    return round((task_selesai / total_task) * 100)


def add_progress_data(data):

    hasil = []

    for item in data:

        agenda = item["agenda"]

        hasil.append(
            {
                "agenda": agenda,
                "deadline_status": item["deadline_status"],
                "progress": get_agenda_progress(agenda[0]),
            }
        )

    return hasil
