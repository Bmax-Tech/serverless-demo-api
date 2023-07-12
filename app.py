import requests
from flask import Flask, jsonify, make_response

currency_api = 'https://api.coindesk.com/v1/bpi/currentprice.json'

app = Flask(__name__)


@app.route("/", methods=["GET"])
def root_handler():
    return jsonify(message='Hello from serverless-demo-api !')


@app.route("/stats", methods=["GET"])
def stats_handler():
    res = requests.get(currency_api)
    return jsonify(message=res.json())


@app.errorhandler(404)
def resource_not_found_handler(e):
    return make_response(jsonify(error='Not found!'), 404)
