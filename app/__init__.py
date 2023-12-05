from flask import Flask
# from config.config import Config

def create_app():
    app = Flask(__name__)
    # app.config.from_object(Config)

    # Configuração dos blueprints
    from app.main.routes import main_bp
    # from app.auth.routes import auth_bp
    # from app.dashboard.routes import dashboard_bp

    app.register_blueprint(main_bp)
    # app.register_blueprint(auth_bp, url_prefix='/auth')
    # app.register_blueprint(dashboard_bp, url_prefix='/dashboard')

    return app
