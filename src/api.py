from flask import Flask
import os
from decouple import config
from scraper import generate_token 

app = Flask(__name__)


# startup
def get_token():
    username = os.getenv('USER')
    password = os.getenv('PASSWORD')
    serial = os.getenv('SERIAL')

    if username is None or password is None or serial is None:
        # use local .env
        username = config('USER')
        password = config('PASSWORD')
        serial = config('SERIAL')

    token = generate_token.generate_token(username, password, serial)
    # raise error if unable to get token
    return token


token = get_token()


@app.route("/metrics")
def metrics():
    return "metrics"
