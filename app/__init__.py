"""flask initializing file"""
from flask import Flask, jsonify
from app.routes import Routes
APP = Flask(__name__)
ROUTES = Routes()
ROUTES.initialize(APP)


@APP.errorhandler(404)
def page_not_found(e):
    """function incase of invalid url"""
    response = jsonify({"message": "use a valid URL"})
    response.status_code = 404
    return response
