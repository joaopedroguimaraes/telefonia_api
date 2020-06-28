from flask import Flask, make_response, jsonify, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint

from routes import api_routes

app = Flask(__name__)

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'api_name': "telefonia_api"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

app.register_blueprint(api_routes.get_blueprint())


@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)


@app.errorhandler(400)
def handle_400_error(_error):
    return make_response(jsonify({'error': 'Misunderstood'}), 400)


@app.errorhandler(404)
def handle_404_error(_error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(500)
def handle_500_error(_error):
    return make_response(jsonify({'error': 'Server error'}), 500)


if __name__ == "__main__":
    app.run()
