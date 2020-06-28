import ast

from bson.json_util import dumps
from flask import Blueprint, json, request, jsonify, send_from_directory

from manager import Manager

manager = Manager()

api = Blueprint('request_api', __name__)


def get_blueprint():
    """Return the blueprint for the main app module"""
    return api


@api.route("/")
def index():
    return api.send_static_file('index.html')


@api.route("/status", methods=['GET'])
def status():
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@api.route("/phones", methods=['GET'])
def get_all_phones():
    query_params = request.args.to_dict()
    if query_params:
        query = {k: int(v) if isinstance(v, str) and v.isdigit() else v for k, v in query_params.items()}

        records_fetched = manager.verify_phones(query)

        if records_fetched.count() > 0:
            return dumps(records_fetched)
        else:
            return "", 404
    else:
        if manager.count() > 0:
            return dumps(manager.get_all_phones())
        else:
            return jsonify([])


@api.route("/phones", methods=['POST'])
def block_phones():
    try:
        try:
            body = ast.literal_eval(json.dumps(request.get_json()))
        except ValueError:
            return "", 400

        if isinstance(body, list) and len(body) == 0:
            return "", 400

        record_inserted = manager.block_phones(body)

        if isinstance(record_inserted, list):
            if len(record_inserted) == 0:
                return dumps(record_inserted), 200
            else:
                return jsonify([v for v in record_inserted]), 200
        else:
            return jsonify(record_inserted), 200
    except KeyError:
        return "", 400
    except:
        return "", 500
    # if request.json is not None:
    #     return jsonify(manager.block_phones(request.get_json()))
    # else:
    #     abort(400)


@api.route("/phones", methods=['DELETE'])
def unblock_phones():
    try:
        try:
            body = ast.literal_eval(json.dumps(request.get_json()))
        except ValueError:
            return "", 400

        if len(body) == 0:
            return "", 400

        record_deleted = manager.unblock_phones(body)

        if isinstance(record_deleted, list):
            if len(record_deleted) == 0:
                return dumps(record_deleted), 200
            else:
                return jsonify([v for v in record_deleted]), 200
        else:
            return jsonify(record_deleted), 200
    except KeyError:
        return "", 400
    except:
        return "", 500


@api.route("/verify", methods=['POST'])
def verify_phones():
    try:
        try:
            body = ast.literal_eval(json.dumps(request.get_json()))
        except ValueError:
            return "", 400

        if len(body) == 0:
            return "", 400

        record_verified = manager.verify_phones(body)

        if isinstance(record_verified, list):
            if len(record_verified) == 0:
                return dumps(record_verified), 200
            else:
                return jsonify([v for v in record_verified]), 200
        else:
            return jsonify(record_verified), 200
    except KeyError:
        return "", 400
    except:
        return "", 500
