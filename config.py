"""
D-Tech Dynamics — Configuration
Environment-based configuration classes used by the application factory.
"""
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Base configuration shared by all environments."""

    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key-change-in-production")

    # Uploads
    UPLOAD_FOLDER = os.path.join(basedir, "uploads")
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5 MB

    # Company info (used across templates)
    COMPANY_NAME = "D-Tech Dynamics"
    COMPANY_TAGLINE = "Forged in Fire. Protected by Code."
    COMPANY_EMAIL = "D-TechDynamics@proton.me"
    COMPANY_PHONE = "+1 (868) 358-0435"

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    ENV = "development"


class ProductionConfig(Config):
    DEBUG = False
    ENV = "production"

    @staticmethod
    def init_app(app):
        Config.init_app(app)
        # Production-only setup (logging, error reporting, etc.) goes here.


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
    "default": DevelopmentConfig,
}
