from .database import get_connection

def create_tasks_table():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        agenda_id INTEGER NOT NULL,
        nama_tugas TEXT NOT NULL,
        status TEXT DEFAULT 'belum',

        FOREIGN KEY(agenda_id)
        REFERENCES agenda(id)
    )
    """)

    conn.commit()
    conn.close()


def count_tasks(agenda_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM tasks
        WHERE agenda_id = ?
        """,
        (agenda_id,),
    )

    total = cursor.fetchone()[0]

    conn.close()

    return total


def add_task(agenda_id, nama_tugas):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO tasks(
            agenda_id,
            nama_tugas
        )
        VALUES (?, ?)
        """,
        (agenda_id, nama_tugas),
    )

    conn.commit()
    conn.close()


def get_tasks(agenda_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM tasks
        WHERE agenda_id = ?
        """,
        (agenda_id,),
    )

    tasks = cursor.fetchall()

    conn.close()

    return tasks


def get_task_by_id(user_id, task_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT tasks.*
        FROM tasks
        JOIN agenda
        ON tasks.agenda_id = agenda.id
        WHERE tasks.id = ?
        AND agenda.user_id = ?
        """,
        (task_id, user_id),
    )

    task = cursor.fetchone()

    conn.close()

    return task


def update_task(user_id, task_id, nama_tugas):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE tasks
        SET nama_tugas = ?
        WHERE id IN (
            SELECT tasks.id
            FROM tasks
            JOIN agenda
            ON tasks.agenda_id = agenda.id
            WHERE tasks.id = ?
            AND agenda.user_id = ?
        ) 
        """,
        (nama_tugas, task_id, user_id),
    )

    conn.commit()
    conn.close()


def delete_task(user_id, task_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM tasks
        WHERE id IN (
            SELECT tasks.id
            FROM tasks
            JOIN agenda
            ON tasks.agenda_id = agenda.id
            WHERE tasks.id = ?
            AND agenda.user_id = ?
        )
        """,
        (task_id, user_id),
    )

    conn.commit()
    conn.close()


def update_task_status(user_id, task_id, status):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE tasks
        SET status = ?
        WHERE id IN (
            SELECT tasks.id
            FROM tasks
            JOIN agenda
            ON tasks.agenda_id = agenda.id
            WHERE tasks.id = ?
            AND agenda.user_id = ?
        )
        """,
        (status, task_id, user_id),
    )

    conn.commit()
    conn.close()


def is_agenda_finished(agenda_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM tasks
        WHERE agenda_id = ?
        """,
        (agenda_id,),
    )

    total_task = cursor.fetchone()[0]

    if total_task == 0:
        conn.close()
        return False

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM tasks
        WHERE agenda_id = ?
        AND status != 'selesai'
        """,
        (agenda_id,),
    )

    total_belum_selesai = cursor.fetchone()[0]

    conn.close()

    return total_belum_selesai == 0
