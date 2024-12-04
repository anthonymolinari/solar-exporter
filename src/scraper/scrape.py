# scrape and format data from inverter local api for prometheus
import requests as req


def get_meter_details(gateway_ip):
    res = req.get(f'http://{gateway_ip}/ivp/meters')
    return res.json()


def get_meter_readings(gateway_ip):
    res = req.get(f'http://{gateway_ip}/ivp/meters/readings')
    return res.json()


def get_production_data(gateway_ip):
    res = req.get(f'http://{gateway_ip}/api/v1/production')
    return res.json()


def get_production_details(gateway_ip):
    res = req.get(f'http://{gateway_ip}/ivp/pdm/energy')
    return res.json()


def get_inverters(gateway_ip):
    res = req.get(f'http://{gateway_ip}/api/v1/production/inverters')
    return res.json()


def get_status(gateway_ip):
    res = req.get(f'http://{gateway_ip}/ivp/livedata/status')
    return res.json()


def get_consumption(gateway_ip):
    res = req.get(f'http://{gateway_ip}/ivp/meters/reports/consumption')
    return res.json()
