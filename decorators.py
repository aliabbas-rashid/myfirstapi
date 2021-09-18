from functools import wraps
from flask import request, make_response


def validate_user(username, password):
    return username == "ali" and password == "abbas"


def authenticate(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not validate_user(auth.username, auth.password):
            resp = make_response("", 401)
            resp.headers["WWW-Authenticate"] = 'Basic realm="Login Required"'
            return  resp
        return func(*args, **kwargs)
    return decorated