#!/bin/python3

from flask import Flask, request, jsonify
import redis
from werkzeug.exceptions import BadRequest, InternalServerError

app = Flask(__name__)
app.config['BUNDLE_ERRORS'] = True
app.debug = True
app.config["DEBUG"] = True

db = redis.Redis('localhost')  # connect to server
ttl = 300  # 5 minute


@app.route('/')
def welcome():
    return jsonify({"message": "Welcome"}), 200


@app.route('/values', methods=['POST'])
def save_values():
    if request.method == 'POST':
        try:
            response_data = request.json
        except BadRequest as exception:
            return jsonify({"message": exception.description}), exception.code
        except InternalServerError as exception:
            return jsonify({"message": exception.description}), exception.code

        if len(response_data) == 0:
            return jsonify({"message": "JSON is empty"}), 400

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

        if 'keys' in request.args:
            keys_arg = request.args.get('keys')

            if len(keys_arg) == 0:
                return jsonify({"message": "Empty Argument 'keys'"}),
            else:
                all_keys = keys_arg.split(sep=',')

        else:
            all_keys = db.keys()
            if len(all_keys) == 0:
                return jsonify({"message": "All expired"}), 410

        response_data = {}
        for key in all_keys:
            key = key.decode("utf-8") if hasattr(key, 'decode') else key
            byte_value = db.get(key)

            if byte_value is None:
                value = "Does not exists"
            else:
                value = byte_value.decode("utf-8")
                db.expire(key, ttl)

            response_data.update({key: value})

        if len(response_data) == 0:
            return jsonify({"message": "All expired"}), 410

        return jsonify(response_data), 200


if __name__ == '__main__':
    app.run(debug=True)
