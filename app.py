from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'NO_KEY'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    db.init_app(app)

    from views import views
    from auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    from models import SUP_User

    with app.app_context():
        db.create_all()


    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return SUP_User.query.get(int(id))


    def interpolate_color(start_color, end_color, percent):
        start_r = int(start_color[0:2], 16)
        start_g = int(start_color[2:4], 16)
        start_b = int(start_color[4:6], 16)
        
        end_r = int(end_color[0:2], 16)
        end_g = int(end_color[2:4], 16)
        end_b = int(end_color[4:6], 16)
        
        interpolated_r = int(start_r - (start_r - end_r) * percent)
        interpolated_g = int(start_g - (start_g - end_g) * percent)
        interpolated_b = int(start_b - (start_b - end_b) * percent)
        
        interpolated_color = f'#{interpolated_r:02X}{interpolated_g:02X}{interpolated_b:02X}'
        
        return interpolated_color
    
    app.jinja_env.globals.update(interpolate_color=interpolate_color)


    return app
