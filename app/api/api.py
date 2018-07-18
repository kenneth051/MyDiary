"""api views"""
from flask import request,jsonify
from flask_restful import Resource
from app.model.diary import Diary
from datetime import date,datetime
from app.validation2 import Validate2

class Create(Resource):
    """API class to enter entries"""
    def post(self):
        """method to create entries"""
        try:
            data = request.get_json()
            valid=Validate2(data["entry_id"], data["title"], data["body"])
            info=valid.validate_empty()
            if info == True:
                obj = Diary(data["entry_id"], data["title"], data["body"])
                info = obj.create()
                return info
            else:
                response = jsonify({"message" : info})
                response.status_code = 400
                return response
        except:
            response = jsonify({"message" : "MISSING OR INCORRECT FIELDS DATA"})
            response.status_code = 400
            return response                           


class All(Resource):
    """API class to get entries"""
    def get(self):
        """method to get entries"""
        data = Diary.all()
        return data


class FetchOne(Resource):
    """API class to get one entry"""
    def get(self, entryid):
        """method to get one entry"""
        data = Diary.single_entry(entryid)
        return data

    def put(self, entryid):
        """method to update an entry"""
        try:
            data = request.get_json()
            valid=Validate2.validate_update(data["title"], data["body"])
            if valid == True:
                result = Diary.update(entryid, data)
                return result
            else:
                response = jsonify({"message" : valid})
                response.status_code = 400
                return response
        except:
            response = jsonify({"message" : "MISSING FIELDS OR INCORRECT FIELDS DATA"})
            response.status_code = 400
            return response
  