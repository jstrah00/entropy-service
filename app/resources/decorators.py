from functools import wraps
from flask import jsonify
from app.resources.logger import logger


def basic_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            result = f(*args, **kwargs)
            return jsonify(result)
        except Exception as e:
            logger.exception(f"Exception raised: {e}")
            if "get_status_code" in dir(e):
                if e.get_status_code() == 500:
                    return jsonify({"Desc": "There was an error"}), 500
                else:
                    return jsonify({"Desc": str(e.get_exception_message())}),\
                        e.get_status_code()
            else:
                return jsonify({"Desc": "There was an error"}), 500
    return wrapper
