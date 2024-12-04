from flask import Flask
from utils.generate_token import get_token

# startup
app = Flask(__name__)
token = get_token()


@app.route("/metrics")
def metrics():
    return f'<h3>{token}</h3>'
