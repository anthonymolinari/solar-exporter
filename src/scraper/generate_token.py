import json
import requests as req


# generate auth token for enphase inverter api access
def generate_token(user, password, envoy_serial):
    print('generating token')

    login_url = 'http://enlighten.enphaseenergy.com/login/login.json?'
    data = {'user[email]': user, 'user[password]': password}

    res = req.post(login_url, data=data)
    res_data = json.loads(res.text)
    print(res_data)

    data = {
        'session_id': res_data['session_id'],
        'serial_num': envoy_serial,
        'username': user
    }

    res = req.post('http://entrez.enphaseenergy.com/tokens', json=data)
    return res.text
