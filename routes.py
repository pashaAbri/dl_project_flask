from flask import Blueprint, request, jsonify

bp = Blueprint("routes", __name__)


@bp.route('/')
def hello_world():
    return 'Hello World!'


@bp.route('/predict', methods=['GET'])
def predict_get():
    return 'Hello, you called the predict GET method'


@bp.route('/predict', methods=['POST'])
def predict_post():
    data = request.json
    data["test"] = "ok"

    # Replace the following line with your model logic
    predictions = data  # todo:: replace with your own model
    return jsonify(predictions)
