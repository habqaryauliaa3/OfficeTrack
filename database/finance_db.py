from .database import get_connection

def create_income_table():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS income(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        tanggal TEXT NOT NULL,
        keterangan TEXT NOT NULL,
        nominal INTEGER NOT NULL,

        FOREIGN KEY(user_id)
        REFERENCES users(id)
    )
    """)

    conn.commit()
    conn.close()


def create_expense_table():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expense(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        tanggal TEXT NOT NULL,
        keterangan TEXT NOT NULL,
        nominal INTEGER NOT NULL,

        FOREIGN KEY(user_id)
        REFERENCES users(id)
    )
    """)

    conn.commit()
    conn.close()


def add_income(user_id, tanggal, keterangan, nominal):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO income(
            user_id,
            tanggal,
            keterangan,
            nominal
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            user_id,
            tanggal,
            keterangan,
            nominal,
        ),
    )

    conn.commit()
    conn.close()


def get_incomes(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM income
        WHERE user_id = ?
        ORDER BY tanggal DESC
        """,
        (user_id,),
    )

    incomes = cursor.fetchall()

    conn.close()

    return incomes


def delete_income(income_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM income
        WHERE id = ?
        """,
        (income_id,),
    )

    conn.commit()
    conn.close()


def add_expense(user_id, tanggal, keterangan, nominal):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO expense(
            user_id,
            tanggal,
            keterangan,
            nominal
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            user_id,
            tanggal,
            keterangan,
            nominal,
        ),
    )

    conn.commit()
    conn.close()


def get_expenses(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM expense
        WHERE user_id = ?
        ORDER BY tanggal DESC
        """,
        (user_id,),
    )

    expenses = cursor.fetchall()

    conn.close()

    return expenses


def delete_expense(expense_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM expense
        WHERE id = ?
        """,
        (expense_id,),
    )

    conn.commit()
    conn.close()


def get_total_income(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT SUM(nominal)
        FROM income
        WHERE user_id = ?
        """,
        (user_id,),
    )

    total = cursor.fetchone()[0]

    conn.close()

    return total or 0


def get_total_expense(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT SUM(nominal)
        FROM expense
        WHERE user_id = ?
        """,
        (user_id,),
    )

    total = cursor.fetchone()[0]

    conn.close()

    return total or 0


def get_balance(user_id):

    return get_total_income(user_id) - get_total_expense(user_id)
