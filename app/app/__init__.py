from flask import Flask
from .config import Config  # We'll define this next

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Import and register routes (we will define this file later)
    from . import routes
    app.register_blueprint(routes.bp)

    return app
