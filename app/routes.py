"""routes file"""
from flask_restful import Api
from app.api.api import All, Create, FetchOne


class Routes():
    """routes class"""
    def initialize(self, APP):
        """method to initialize route api"""
        API = Api(APP)
        API.add_resource(All, "/API/v1/entries")
        API.add_resource(Create, "/API/v1/entries")
        API.add_resource(FetchOne, "/API/v1/entries/<int:entryid>")
