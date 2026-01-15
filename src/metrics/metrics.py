# scrape and format data from inverter local api for prometheus
import requests as req
# from utils.format_data import format_data


def get_all_data(gateway_ip, token):
    urls = [
        f'http://{gateway_ip}:80/ivp/meters/readings',
        f'http://{gateway_ip}:80/api/v1/production',
        f'http://{gateway_ip}:80/ivp/pdm/energy',
        f'http://{gateway_ip}:80/api/v1/production/inverters',
        f'http://{gateway_ip}:80/ivp/meters/reports/consumption'
    ]
    data = []

    for u in urls:
        res = req.get(url=u, headers={"Authorization": f"Bearer {token}"}, verify=False)
        data.append(res.json())

    return data


def get_inverters(gateway_ip, token) -> str:
    url = f'http://{gateway_ip}/api/v1/production/inverters'
    res = req.get(
            url=url,
            headers={"Authorization": f"Bearer {token}"},
            verify=False
    )
    data = res.json()
    '''
    data_str = ""
    for i in data:
        for key in i.keys():
            data_str += str(f"{key} = {str(i[key])}\n")
    '''

    return data
