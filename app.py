#!/bin/python3

from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)


@app.route('/')
def welcome():
    return "Welcome"


if __name__ == '__main__':
    app.run(debug=True)
