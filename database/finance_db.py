from .database import get_connection

def create_income_table():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS income(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        kategori TEXT NOT NULL,
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
        kategori TEXT NOT NULL,
        tanggal TEXT NOT NULL,
        keterangan TEXT NOT NULL,
        nominal INTEGER NOT NULL,

        FOREIGN KEY(user_id)
        REFERENCES users(id)
    )
    """)

    conn.commit()
    conn.close()


def add_income(user_id, kategori, tanggal, keterangan, nominal):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO income(
            user_id,
            kategori,
            tanggal,
            keterangan,
            nominal
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            user_id,
            kategori,
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


def delete_income(user_id, income_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM income
        WHERE id = ?
        AND user_id = ?
        """,
        (income_id, user_id),
    )

    conn.commit()
    conn.close()


def add_expense(user_id, kategori, tanggal, keterangan, nominal):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO expense(
            user_id,
            kategori,
            tanggal,
            keterangan,
            nominal
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            user_id,
            kategori,
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


def delete_expense(user_id, expense_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM expense
        WHERE id = ?
        AND user_id = ?
        """,
        (expense_id, user_id),
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

def get_monthly_summary(user_id, bulan, tahun):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT SUM(nominal)
        FROM income
        WHERE user_id = ?
        AND strftime('%m', tanggal) = ?
        AND strftime('%Y', tanggal) = ?
        """,
        (
            user_id,
            bulan,
            tahun,
        ),
    )

    income = cursor.fetchone()[0] or 0

    cursor.execute(
        """
        SELECT SUM(nominal)
        FROM expense
        WHERE user_id = ?
        AND strftime('%m', tanggal) = ?
        AND strftime('%Y', tanggal) = ?
        """,
        (
            user_id,
            bulan,
            tahun,
        ),
    )

    expense = cursor.fetchone()[0] or 0
    conn.close()

    balance = income - expense

    return {
        "monthly_income": income,
        "monthly_expense": expense,
        "monthly_balance": balance,
    }


def get_income_chart_data(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            kategori,
            SUM(nominal)
        FROM income
        WHERE user_id = ?
        GROUP BY kategori
        ORDER BY kategori
        """,
        (user_id,),
    )

    rows = cursor.fetchall()

    conn.close()

    labels = []
    data = []

    for row in rows:
        labels.append(row[0])
        data.append(row[1])

    return {
        "labels": labels,
        "data": data,
    }


def get_expense_chart_data(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            kategori,
            SUM(nominal)
        FROM expense
        WHERE user_id = ?
        GROUP BY kategori
        ORDER BY kategori
        """,
        (user_id,),
    )

    rows = cursor.fetchall()

    conn.close()

    labels = []
    data = []

    for row in rows:
        labels.append(row[0])
        data.append(row[1])

    return {
        "labels": labels,
        "data": data,
    }
