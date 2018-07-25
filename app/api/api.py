"""api views"""
import uuid
from flask import Flask, request, jsonify
from app.model.diary import Diary
from app.validation2 import Validate2

APP = Flask(__name__)


@APP.route('/API/v1/entries', methods=['POST'])
def create_entries():
    """method to create entries"""
    try:
        data = request.get_json()
        valid = Validate2(data["title"], data["body"])
        info = valid.validate_empty()
        if info is True:
            entry_id = int(str(uuid.uuid1().int)[:8])
            obj = Diary(entry_id, data["title"], data["body"])
            info = obj.creating_entry()
            return info
        else:
            response = jsonify({"message": info})
            response.status_code = 400
            return response
    except:
        response = jsonify({"message": "DATA FIELDS ISSUE"})
        response.status_code = 400
        return response


@APP.route('/API/v1/entries', methods=['GET'])
def get_entries():
    """method to get entries"""
    data = Diary.all_entries()
    return data


@APP.route('/API/v1/entries/<int:entryid>', methods=['GET'])
def get_entry(entryid):
    """method to get one entry"""
    data = Diary.single_entry(entryid)
    return data


@APP.route('/API/v1/entries/<int:entryid>', methods=['PUT'])
def update_entry(entryid):
    """method to update an entry"""
    try:
        data = request.get_json()
        valid = Validate2(data["title"], data["body"])
        info = valid.validate_empty()
        if info is True:
            result = Diary.updating_entry(entryid, data)
            return result
        else:
            response = jsonify({"message": info})
            response.status_code = 400
            return response
    except:
        response = jsonify({"message": "DATA FIELDS ISSUE"})
        response.status_code = 400
        return response


@APP.errorhandler(404)
def page_not_found(e):
    """function incase of invalid url"""
    response = jsonify({"message": "use a valid URL"})
    response.status_code = 404
    return response
