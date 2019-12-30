#!/bin/python3

from flask import Flask, request, jsonify
import redis

app = Flask(__name__)
app.config['BUNDLE_ERRORS'] = True
app.debug = True

db = redis.Redis('localhost')  # connect to server
ttl = 300  # 5 minute


@app.route('/')
def welcome():
    return jsonify({"message": "Welcome"}), 200


@app.route('/values', methods=['POST'])
def save_values():
    if request.method == 'POST':
        response_data = request.json

        update_value_dict = {}
        for key, value in response_data.items():
            flag = db.set(key, value, ex=ttl, nx=True)

            if flag is None:
                current_value = db.get(key).decode("utf-8")
                message = "Already exists"
            else:
                current_value = value
                message = "Success"

            update_value_dict.update({
                key: dict(
                    value=current_value,
                    message=message,
                    ttl=db.ttl(key)
                )
            }
            )

        response_data.update(update_value_dict)

    return jsonify(response_data), 201


@app.route('/values', methods=['GET'])
def get_values():
    if request.method == 'GET':

        all_keys = db.keys()
        if len(all_keys) == 0:
            return jsonify({"message": "All expired"}), 404

        response_data = {}
        for key in all_keys:
            key = key.decode("utf-8")
            value = db.get(key).decode("utf-8")
            db.expire(key, ttl)
            response_data.update({key: value})

        return jsonify(response_data), 200


if __name__ == '__main__':
    app.run(debug=True)
