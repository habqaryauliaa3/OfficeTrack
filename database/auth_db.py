from .database import get_connection

def create_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama TEXT NOT NULL,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()


def register_user(nama, username, password):
    conn = get_connection()
    cursor = conn.cursor()

    # cek username sudah ada atau belum
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))

    user = cursor.fetchone()

    if user:
        conn.close()
        return False

    cursor.execute(
        """
    INSERT INTO users (nama, username, password)
    VALUES (?, ?, ?)
    """,
        (nama, username, password),
    )

    conn.commit()
    conn.close()

    return True


def login_user(username):

    conn = get_connection()

    user = conn.execute(
        """
        SELECT *
        FROM users
        WHERE username = ?
        """,
        (username,),
    ).fetchone()

    conn.close()

    return user
