from flask import request, jsonify
from flask_restful import Resource
from diary import Diary

class Create(Resource):
    def post(self):
        data=request.get_json()
        obj=Diary(data["id"],data["title"],data["date"],data["time"],data["body"])
        info=obj.create()
        return jsonify({"You have entered an entry":info})
class All(Resource):
    def get(self):
        data=Diary.all()
        return jsonify({"Results":data})
class FetchOne(Resource):
    def get(self,entryId):
        data=Diary.singleEntry(entryId)
        return jsonify({"result":data})

    def put(self,entryId):
        data=request.get_json()
        result=Diary.update(entryId,data)
        return result
           
   


                
       