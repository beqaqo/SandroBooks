from flask import Flask
from src.admin_views import BookView
from src.admin_views.base import SecureModelView
from src.config import Config
from src.ext import db, migrate, login_manager, admin, api
from src.views import  auth_blueprint
from src.commands import init_db, populate_db
from src.models.user import User
from src.models.series import Series
from src.models.book import Book
from src.models.project import Project
import src.endpoints.project.project_api
from src.models.faq import FrequentlyAskedQuestion
import src.admin_views
import src.endpoints.book.book_api
import src.endpoints.faq.faq_api

BLUEPRINTS = [auth_blueprint]
COMMANDS = [init_db, populate_db]

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    return app

def register_extensions(app):
    # Flask-SQLAlchemy
    db.init_app(app)

    # Flask-Migrate
    migrate.init_app(app, db)

    #Flask-Login
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(_id):
        return User.query.get(_id)

    # Flask_admin
    admin.init_app(app)
    admin.add_view(BookView(Book, db.session, name="Books Default", endpoint="books_default"))
    src.admin_views.register_admin_views(admin, db)

    #Flask_RestX
    api.init_app(app)

def register_blueprints(app):
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)

def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)