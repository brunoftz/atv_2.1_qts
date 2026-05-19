from flask import Blueprint, jsonify

health_bp = Blueprint("health", __name__)


@health_bp.route("/status", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"})


@health_bp.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello World"})
