from flask import Flask
from flask_restful import Api
from api import All,Create,FetchOne
APP= Flask(__name__)
API=Api(APP)
API.add_resource(All, "/API/v1/entries")
API.add_resource(Create, "/API/v1/entries")
API.add_resource(FetchOne, "/API/v1/entries/<int:entryid>")

if __name__ == '__main__':
    APP.run(debug=True)
