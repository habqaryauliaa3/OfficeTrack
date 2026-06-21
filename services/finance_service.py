# services/finance_service.py

from database.finance_db import *
from services.activity_service import *


def create_income_service(user_id, tanggal, keterangan, nominal):
    add_income(user_id, tanggal, keterangan, nominal)

    add_log(user_id, f"Menambahkan pemasukan: {keterangan}")


def create_expense_service(user_id, tanggal, keterangan, nominal):
    add_expense(user_id, tanggal, keterangan, nominal)

    add_log(user_id, f"Menambahkan pengeluaran: {keterangan}")


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
