import json
import requests as req
import os
from decouple import config


# generate auth token for enphase inverter api access
def generate_token(user, password, envoy_serial):
    print('generating token')

    login_url = 'http://enlighten.enphaseenergy.com/login/login.json?'
    data = {'user[email]': user, 'user[password]': password}

    res = req.post(login_url, data=data)
    res_data = json.loads(res.text)

    data = {
        'session_id': res_data['session_id'],
        'serial_num': envoy_serial,
        'username': user
    }

    res = req.post('http://entrez.enphaseenergy.com/tokens', json=data)
    return res.text


def get_token():
    username = os.getenv('USER')
    password = os.getenv('PASSWORD')
    serial = os.getenv('SERIAL')

    if username is None or password is None or serial is None:
        # use local .env
        username = config('USER')
        password = config('PASSWORD')
        serial = config('SERIAL')

    token = generate_token(username, password, serial)
    print(f" token generated: {token}")
    # raise error if unable to get token
    return token
