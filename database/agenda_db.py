from .task_db import is_agenda_finished
from .database import get_connection

def create_agenda_table():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS agenda(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        judul TEXT NOT NULL,
        deskripsi TEXT,
        tanggal TEXT NOT NULL,
        prioritas INTEGER DEFAULT 0,

        FOREIGN KEY(user_id)
        REFERENCES users(id)
    )
    """)

    conn.commit()
    conn.close()


def add_agenda(user_id, judul, deskripsi, tanggal, prioritas):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
    INSERT INTO agenda(
        user_id,
        judul,
        deskripsi,
        tanggal,
        prioritas
    )
    VALUES (?, ?, ?, ?, ?)
    """,
        (user_id, judul, deskripsi, tanggal, prioritas),
    )

    conn.commit()
    conn.close()


def get_agendas(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
    SELECT *
    FROM agenda
    WHERE user_id = ?
    ORDER BY prioritas DESC, tanggal ASC
    """,
        (user_id,),
    )

    agendas = cursor.fetchall()

    conn.close()

    return agendas


def get_active_agendas(user_id):

    agendas = get_agendas(user_id)

    active_agendas = []

    for agenda in agendas:

        if not is_agenda_finished(agenda[0]):
            active_agendas.append(agenda)

    return active_agendas


def get_finished_agendas(user_id):

    agendas = get_agendas(user_id)

    finished_agendas = []

    for agenda in agendas:

        if is_agenda_finished(agenda[0]):
            finished_agendas.append(agenda)

    return finished_agendas


def search_agendas(user_id, keyword):

    conn = get_connection()
    cursor = conn.cursor()

    keyword = f"%{keyword}%"

    cursor.execute(
        """
        SELECT *
        FROM agenda
        WHERE user_id = ?
        AND (
            judul LIKE ?
            OR deskripsi LIKE ?
        )
        ORDER BY prioritas DESC, tanggal ASC
        """,
        (
            user_id,
            keyword,
            keyword,
        ),
    )

    agendas = cursor.fetchall()

    conn.close()

    return agendas


def filter_agendas(user_id, keyword, status, prioritas):

    agendas = search_agendas(user_id, keyword)

    if status == "aktif":

        agendas = [agenda for agenda in agendas if not is_agenda_finished(agenda[0])]

    elif status == "selesai":

        agendas = [agenda for agenda in agendas if is_agenda_finished(agenda[0])]

    if prioritas == "prioritas":

        agendas = [agenda for agenda in agendas if agenda[5] == 1]

    elif prioritas == "normal":

        agendas = [agenda for agenda in agendas if agenda[5] == 0]

    return agendas


def get_agenda_by_id(user_id, agenda_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
    SELECT *
    FROM agenda
    WHERE id = ?
    AND user_id = ?
    """,
        (
            agenda_id,
            user_id,
        ),
    )

    agenda = cursor.fetchone()

    conn.close()

    return agenda


def update_agenda(user_id, agenda_id, judul, deskripsi, tanggal, prioritas):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE agenda
        SET
            judul = ?,
            deskripsi = ?,
            tanggal = ?,
            prioritas = ?
        WHERE id = ?
        AND user_id = ?
        """,
        (judul, deskripsi, tanggal, prioritas, agenda_id, user_id),
    )

    conn.commit()
    conn.close()


def count_agendas(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
    SELECT COUNT(*)
    FROM agenda
    WHERE user_id = ?
    """,
        (user_id,),
    )

    total = cursor.fetchone()[0]

    conn.close()

    return total


def delete_agenda(user_id, agenda_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM agenda
        WHERE id = ?
        AND user_id = ?
        """,
        (
            agenda_id,
            user_id
        ),
    )

    conn.commit()
    conn.close()


def count_active_agendas(user_id):

    agendas = get_agendas(user_id)

    total = 0

    for agenda in agendas:

        if not is_agenda_finished(agenda[0]):
            total += 1

    return total


def count_finished_agendas(user_id):

    agendas = get_agendas(user_id)

    total = 0

    for agenda in agendas:

        if is_agenda_finished(agenda[0]):
            total += 1

    return total
