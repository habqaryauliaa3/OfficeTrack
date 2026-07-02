# services/finance_service.py

from database.finance_db import *
from services.activity_service import *

INCOME_CATEGORIES = [
    "Uang Saku",
    "THR",
    "Bonus",
    "Kas",
    "Lainnya",
]

EXPENSE_CATEGORIES = [
    "Transport",
    "Makan",
    "Internet",
    "ATK",
    "Fotokopi",
    "Lainnya",
]


def validate_nominal(nominal):

    nominal = int(nominal)

    if nominal <= 0:
        return "Nominal harus lebih dari 0"

    return None


def validate_keterangan(keterangan):

    if not keterangan.strip():
        return "Keterangan wajib diisi"

    if len(keterangan) > 150:
        return "Keterangan terlalu panjang"

    return None


def create_income_service(user_id, kategori, tanggal, keterangan, nominal):
    error = validate_nominal(nominal)
    if error:
        return error

    error = validate_keterangan(keterangan)
    if error:
        return error

    add_income(user_id, kategori, tanggal, keterangan, nominal)

    add_log(user_id, f"Menambahkan pemasukan: {keterangan}")

    return None


def create_expense_service(user_id, kategori, tanggal, keterangan, nominal):
    error = validate_nominal(nominal)
    if error:
        return error

    error = validate_keterangan(keterangan)
    if error:
        return error

    add_expense(user_id, kategori, tanggal, keterangan, nominal)

    add_log(user_id, f"Menambahkan pengeluaran: {keterangan}")

    return None

def delete_income_service(user_id, income_id):
    delete_income(income_id)

    add_log(user_id, "Menghapus pemasukan")


def delete_expense_service(user_id, expense_id):
    delete_expense(expense_id)

    add_log(user_id, "Menghapus pengeluaran")


def get_finance_summary_service(user_id):

    incomes = get_incomes(user_id)

    expenses = get_expenses(user_id)

    total_income = get_total_income(user_id)

    total_expense = get_total_expense(user_id)

    balance = get_balance(user_id)

    return {
        "incomes": incomes,
        "expenses": expenses,
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": balance,
    }


def get_income_categories():
    return INCOME_CATEGORIES


def get_expense_categories():
    return EXPENSE_CATEGORIES


def get_monthly_summary_service(
    user_id,
    bulan,
    tahun,
):
    return get_monthly_summary(
        user_id,
        bulan,
        tahun,
    )


def get_income_chart_data_service(user_id):
    return get_income_chart_data(user_id)


def get_expense_chart_data_service(user_id):
    return get_expense_chart_data(user_id)
