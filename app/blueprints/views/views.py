"""Module designated for API endpoints"""

from flask import Blueprint, request
from app.entropy import entropy
from app.resources.exceptions import MissingFileException
from app.resources.decorators import basic_decorator

views = Blueprint("views", __name__)
DEFAULT_BLOCK_SIZE = 1024


@views.route("/entropy", methods=["POST"])
@basic_decorator
def generate_entropy_report() -> request:
    """Generate file entropy report"""
    # file is required
    if 'file' not in request.files or request.files['file'].filename == '':
            raise MissingFileException
    # set blocksize to default if not specified
    if 'blocksize' not in request.form:
        block_size = DEFAULT_BLOCK_SIZE
    else:
        block_size = int(request.form['blocksize'])
    uploaded_file = request.files['file']
    uploaded_file.save(uploaded_file.filename)
    response = entropy.generate_entropy_report(
        uploaded_file.filename, block_size)
    return response
