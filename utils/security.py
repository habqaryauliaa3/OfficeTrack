# utils/security.py

from functools import wraps
from flask import session, redirect

from werkzeug.security import generate_password_hash, check_password_hash

def hash_password(password):
    return generate_password_hash(password)


def verify_password(hash_pw, password):
    return check_password_hash(hash_pw, password)


def login_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        if "user_id" not in session:
            return redirect("/login")

        return func(*args, **kwargs)

    return wrapper
