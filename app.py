from flask import Flask

from routes.auth import auth_bp
from routes.dashboard import dashboard_bp
from routes.agenda import agenda_bp
from routes.finance import finance_bp
from routes.logs import logs_bp

from database.auth_db import create_database
from database.agenda_db import create_agenda_table
from database.task_db import create_tasks_table
from database.log_db import create_activity_logs_table
from database.finance_db import create_income_table, create_expense_table

from utils.filters import rupiah, tanggal

app = Flask(__name__)

app.jinja_env.filters["rupiah"] = rupiah
app.jinja_env.filters["tanggal"] = tanggal
app.secret_key = "officetrack_secret_key"

# database setup
create_database()
create_agenda_table()
create_tasks_table()
create_activity_logs_table()
create_income_table()
create_expense_table()

# register blueprint
app.register_blueprint(auth_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(agenda_bp)
app.register_blueprint(finance_bp)
app.register_blueprint(logs_bp)

if __name__ == "__main__":
    app.run(debug=True)
