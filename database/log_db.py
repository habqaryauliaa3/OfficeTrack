from datetime import datetime
from .database import get_connection

def create_activity_logs_table():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS activity_logs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        aktivitas TEXT NOT NULL,
        tanggal TEXT NOT NULL,

        FOREIGN KEY(user_id)
        REFERENCES users(id)
    )
    """)

    conn.commit()
    conn.close()


def add_log(user_id, aktivitas):

    conn = get_connection()
    cursor = conn.cursor()

    tanggal = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute(
        """
        INSERT INTO activity_logs(
            user_id,
            aktivitas,
            tanggal
        )
        VALUES (?, ?, ?)
        """,
        (user_id, aktivitas, tanggal),
    )

    conn.commit()
    conn.close()


def get_logs(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM activity_logs
        WHERE user_id = ?
        ORDER BY tanggal DESC
        """,
        (user_id,),
    )

    logs = cursor.fetchall()

    conn.close()

    return logs
