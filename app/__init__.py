import os
from flask import Flask
from app.extensions import db, login_manager
from app.routes.auth import auth
from app.routes.dashboard import dashboard
from app.routes.attendance import attendance
from app.routes.reports import reports
from app.routes.employees import employees
from app.models import User

def create_app():
    base_dir = os.path.abspath(os.path.dirname(__file__))

    app = Flask(__name__,
                template_folder=os.path.join(base_dir, '..', 'templates'),
                static_folder=os.path.join(base_dir, '..', 'static'))

    app.config.from_mapping(
        SECRET_KEY='your-secret-key',
        SQLALCHEMY_DATABASE_URI='postgresql://postgres:admin@localhost/adpsystem',
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    app.register_blueprint(auth)
    app.register_blueprint(dashboard)
    app.register_blueprint(attendance)
    app.register_blueprint(reports)
    app.register_blueprint(employees)

    return app
