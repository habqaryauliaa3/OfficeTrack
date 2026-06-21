# services/dashboard_service.py

from database.agenda_db import *


def get_dashboard_data(user_id):

    daftar_agenda = get_agendas(user_id)

    agenda_aktif = count_active_agendas(user_id)

    agenda_selesai = count_finished_agendas(user_id)

    return {
        "daftar_agenda": daftar_agenda,
        "agenda_aktif": agenda_aktif,
        "agenda_selesai": agenda_selesai,
    }
