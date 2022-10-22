from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from models import create_query, ManyRequestParams

main_bp = Blueprint('main_bp', __name__)


@main_bp.route('/perform_query', methods=['POST'])
def perform_query():
    try:
        params = ManyRequestParams().load(request.json)
    except ValidationError as e:
        return e.messages, 400

    result = None
    for query in params["queries"]:
        result = create_query(
            cmd=query["cmd"],
            param=query["value"],
            data=result
        )
    return jsonify(result)
