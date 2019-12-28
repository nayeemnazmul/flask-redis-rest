#!/bin/python3

from flask import Flask
from flask_restful import Api, Resource, reqparse
import redis

app = Flask(__name__)
app.config['BUNDLE_ERRORS'] = True
app.debug = True
db = redis.Redis('localhost') #connect to server
api = Api(app)

ttl = 60 # 1 minute


@app.route('/')
def welcome():
    return "Welcome"


class KeyValuesAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser(bundle_errors=True)
        self.reqparse.add_argument(type=dict, location='json')
        super(KeyValuesAPI, self).__init__()

    def post(self, value_dict):
        pass
        

api.add_resource(KeyValuesAPI, '/values', endpoint='values')

if __name__ == '__main__':
    app.run(debug=True)
