#!/bin/python3

from flask import Flask, request, jsonify
import redis

app = Flask(__name__)
app.config['BUNDLE_ERRORS'] = True
app.debug = True
db = redis.Redis('localhost') #connect to server
ttl = 300  # 5 minute


@app.route('/')
def welcome():
    return "Welcome"


@app.route('/values', methods=['POST'])
def save_values():
    if request.method == 'POST':
        response_data = request.json

        update_value_dict = {}
        for key, value in response_data.items():
            flag = db.set(key, value, ex=ttl, nx=True)

            if flag is None:
                update_value_dict.update({key: "Already exists"})

        response_data.update(update_value_dict)

    return jsonify(response_data), 201


if __name__ == '__main__':
    app.run(debug=True)
