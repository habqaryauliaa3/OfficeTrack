# services/log_service.py

from database.log_db import *


def get_logs_service(user_id):
    return get_logs(user_id)
