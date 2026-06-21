# services/auth_service.py

from database.auth_db import *


def register_service(nama, username, password):
    return register_user(nama, username, password)


def login_service(username, password):
    return login_user(username, password)


def logout_service():
    return True
