"""Flask app creation."""

from flask import Flask
from app.blueprints.index import ping
from app.blueprints.views import views

# Active endpoints noted as following:
# (url_prefix, blueprint_object)
ACTIVE_ENDPOINTS = (("/", ping), ("/API", views))


def create_app():
    """Create Flask app."""
    flask_app = Flask(__name__)
    # accepts both /endpoint and /endpoint/ as valid URLs
    flask_app.url_map.strict_slashes = False

    # register each active blueprint
    for url, blueprint in ACTIVE_ENDPOINTS:
        flask_app.register_blueprint(blueprint, url_prefix=url)
    return flask_app
