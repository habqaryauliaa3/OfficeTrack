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


def get_agenda_by_id(agenda_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM agenda
        WHERE id = ?
        """,
        (agenda_id,),
    )

    agenda = cursor.fetchone()

    conn.close()

    return agenda


def update_agenda(agenda_id, judul, deskripsi, tanggal, prioritas):

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
        """,
        (judul, deskripsi, tanggal, prioritas, agenda_id),
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


def delete_agenda(agenda_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM agenda
        WHERE id = ?
        """,
        (agenda_id,),
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
