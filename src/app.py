from flask import Flask
from utils.generate_token import get_token
from metrics.metrics import get_all_data, get_inverters

import os
from decouple import config


# startup
app = Flask(__name__)
token = get_token()
gateway_ip = os.getenv('GATEWAY_IP')
if gateway_ip is None:
    gateway_ip = config('GATEWAY_IP')


@app.route("/metrics")
def metrics():
    body = get_all_data(gateway_ip, token)
    return body


@app.route("/metrics/inverters")
def metrics_inverters():
    body = get_inverters(gateway_ip, token)
    return body


@app.route("/health")
def health():
    return "ok"
