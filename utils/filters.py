# utils/filters.py

from datetime import datetime


def rupiah(value):
    return f"Rp {value:,}"


def tanggal(value):
    tanggal_obj = datetime.strptime(value, "%Y-%m-%d")

    return tanggal_obj.strftime("%d-%m-%Y")
