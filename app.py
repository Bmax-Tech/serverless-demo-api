from flask import Flask, jsonify, make_response
from boto3 import client

bucket_name = 'arn:aws:s3:us-east-1:141158507881:accesspoint/serverless-demo-static-ap'
file_name = 'Air_Quality.csv'

app = Flask(__name__)


@app.route("/", methods=["GET"])
def root_handler():
    return jsonify(message='Hello from serverless-demo-api !')


@app.route("/stats", methods=["GET"])
def stats_handler():
    s3 = client('s3')
    obj = s3.get_object(Bucket=bucket_name, Key=file_name)
    return jsonify(message=obj['ETag'])


@app.errorhandler(404)
def resource_not_found_handler(e):
    return make_response(jsonify(error='Not found!'), 404)
