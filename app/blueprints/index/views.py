"""Module with index and ping endpoints."""
from flask import Blueprint, render_template

ping = Blueprint("ping", __name__)


@ping.route("/ping")
def main() -> str:
    """Ping endpoint, used to know if the app is up."""

    return "pong"


@ping.route("/")
def index() -> str:
    """Index file"""

    return render_template('index.html')
