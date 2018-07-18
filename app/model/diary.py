"""Diary class"""
from flask import jsonify
from app.validation1 import Validate
from datetime import date,datetime

class Diary():
    """class with diary attributes"""

    entries = []

    def __init__(self, entry_id, title, body):
        """initializing constructor"""
        self.entry_id = entry_id
        self.title = title
        self.body = body
        self.updated = "-"
    def create(self):
        """method to create entries"""
        today = str(date.today())
        t = str(datetime.time(datetime.now()))
        entry = Diary(self.entry_id, self.title, self.body)
        lst = {}
        lst["entry_id"] = entry.entry_id
        lst["title"] = entry.title
        lst["date"] = today
        lst["time"] = t
        lst["body"] = entry.body
        lst["updated"] = entry.updated
        if Validate.validate_id(Diary.entries, self.entry_id):
            response = jsonify({"message" : "Id has been taken,try again"})
            response.status_code = 409
            return response
        if Validate.validate_entry(Diary.entries, entry):
            response = jsonify({"message" : "Duplicate data,Try again"})
            response.status_code = 409
            return response
        else:
            Diary.entries.append(lst)
            response = jsonify({"message" : "Entry saved", "data" : lst})
            response.status_code = 201
            return response

    @classmethod
    def all(cls):
        """method to get all entries"""
        info = Diary.entries
        response = jsonify({"data" : info})
        response.status_code = 200
        return response

    @classmethod
    def single_entry(cls, entryid):
        """method to get single entry"""
        data = "invalid Id,Try again"
        response = jsonify({"data":data})
        response.status_code = 422
        for info in Diary.entries:
            if info['entry_id'] == entryid:
                response = jsonify({"data" : info})
                response.status_code = 200
        return response

    @classmethod
    def update(cls, entryid, data):
        """method to update entries"""
        result = "invalid Id, cannot update"
        response = jsonify({"data" : result})
        response.status_code = 422
        now = datetime.now()
        new_date = now.strftime("%c")
        for info in Diary.entries:
            if info['entry_id'] == entryid:
                info["title"] = data["title"]
                info["body"] = data["body"]
                info["updated"] = new_date
                result = "update successful"
                response = jsonify({"data" : info, "message" : "updated successfuly"})
                response.status_code = 200
        return response
