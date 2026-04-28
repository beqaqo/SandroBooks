from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_admin import Admin
from src.admin_views.base import SecureIndexView
from flask_restx import Api

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
admin = Admin(index_view=SecureIndexView())
api = Api(title="SB")

