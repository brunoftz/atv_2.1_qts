from flask import Flask


def create_app():
    app = Flask(__name__)

    from app.routes.user_routes import user_bp
    from app.routes.health_routes import health_bp

    app.register_blueprint(user_bp)
    app.register_blueprint(health_bp)

    return app
