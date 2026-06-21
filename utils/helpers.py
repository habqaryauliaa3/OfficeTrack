# utils/helpers.py


def format_rupiah(nominal):
    return f"Rp {nominal:,}"


def yes_no(value):
    return "Ya" if value else "Tidak"
