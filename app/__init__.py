from pathlib import Path

from flask import Flask


def create_app():
    template_dir = Path(__file__).resolve().parent.parent / "templates"
    app = Flask(__name__, template_folder=str(template_dir))

    from app.routes.user_routes import user_bp
    from app.routes.health_routes import health_bp
    from app.routes.web_routes import web_bp

    app.register_blueprint(user_bp)
    app.register_blueprint(health_bp)
    app.register_blueprint(web_bp)

    return app
