"""
D-Tech Dynamics — Application Factory
"""
from flask import Flask, render_template

from config import config


def create_app(config_name="default"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    register_blueprints(app)
    register_error_handlers(app)
    register_context_processors(app)

    return app


def register_blueprints(app):
    from app.routes.main import main_bp

    app.register_blueprint(main_bp)


def register_error_handlers(app):
    @app.errorhandler(404)
    def not_found(error):
        return render_template("errors/404.html"), 404

    @app.errorhandler(500)
    def server_error(error):
        return render_template("errors/500.html"), 500


def register_context_processors(app):
    """Make site-wide values (nav links, company info) available to every template."""

    @app.context_processor
    def inject_globals():
        return {
            "company_name": app.config["COMPANY_NAME"],
            "company_tagline": app.config["COMPANY_TAGLINE"],
            "company_email": app.config["COMPANY_EMAIL"],
            "company_phone": app.config["COMPANY_PHONE"],
            "nav_links": [
                {"label": "Home", "endpoint": "main.index"},
                {"label": "About", "endpoint": "main.about"},
                {"label": "Services", "endpoint": "main.services"},
                {"label": "Portfolio", "endpoint": "main.portfolio"},
                {"label": "Contact", "endpoint": "main.contact"},
            ],
        }
