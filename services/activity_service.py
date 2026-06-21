from database.log_db import add_log


def log_create_agenda(user_id, judul):
    add_log(user_id, f"Membuat agenda: {judul}")


def log_edit_agenda(user_id, judul):
    add_log(user_id, f"Mengedit agenda: {judul}")


def log_delete_agenda(user_id, judul):
    add_log(user_id, f"Menghapus agenda: {judul}")


def log_create_task(user_id, nama_tugas):
    add_log(user_id, f"Menambahkan tugas: {nama_tugas}")


def log_edit_task(user_id, nama_tugas):
    add_log(user_id, f"Mengedit tugas: {nama_tugas}")


def log_delete_task(user_id, nama_tugas):
    add_log(user_id, f"Menghapus tugas: {nama_tugas}")


def log_change_task_status(user_id, nama_tugas, status):
    add_log(user_id, f"Mengubah status tugas '{nama_tugas}' menjadi {status}")
