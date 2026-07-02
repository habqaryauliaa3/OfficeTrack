# services/auth_service.py

from database.auth_db import *
from utils.security import hash_password
from utils.security import verify_password

def register_service(nama, username, password):

    hashed_password = hash_password(password)

    return register_user(nama, username, hashed_password)


def login_service(username, password):

    user = login_user(username)

    if not user:
        return None

    if verify_password(user["password"], password):
        return user

    return None


def logout_service():
    return True
