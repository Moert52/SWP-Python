from flask import Flask, jsonify, request
from flask_restful import Resource, Api

import SteinScherePapier as ssp

app = Flask(__name__)
# creating an API object
api = Api(app)

class StatistikWeb(Resource):
    def get(self):
        list = ssp.readJson()
        return list

api.add_resource(StatistikWeb, '/')

def main():
    app.run(debug=True)  # debug=True lädt nach den Änderungen neu

if __name__ == '__main__':
    main()
