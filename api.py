"""api views"""
from flask import request
from flask_restful import Resource
from diary import Diary

class Create(Resource):
    """API class to enter entries"""
    def post(self):
        """method to create entries"""
        data = request.get_json()
        obj = Diary(data["entry_id"], data["title"], data["date"], data["time"], data["body"])
        info = obj.create()
        return info


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
        data = request.get_json()
        result = Diary.update(entryid, data)
        return result
  