#!/usr/bin/python3.8

import requests
import json
from prettytable import PrettyTable

IP = '92.222.129.112'

CONFIG = {
    'X-Force': {
        'auth': {
            'APIKEY': 'a8b7c39d-9be8-4174-81a2-3860d9230c1b',
            'APIPASS': '221870d2-362f-4d16-bace-f3c8b0d58f94'
        },
        'URL': {
            'ipr': 'https://exchange.xforce.ibmcloud.com/api/ipr/'
        }
    },
    '2ip': {
        'URL': {
            'hosting': 'https://api.2ip.ua/hosting.json?site=',
            'geo': 'https://api.2ip.ua/geo.json?ip=',
            'provider': 'https://api.2ip.ua/provider.json?ip='
        }
    }
}

report = {}


def get_resp(**dicts):
    try:
        if dicts['auth'] != None:
            user = dicts['auth']['APIKEY']
            passwd = dicts['auth']['APIPASS']
            
            res = requests.get(f"{dicts['url']}{dicts['ip']}", auth=(user, passwd))
            return res.json()
        else:
            res = requests.get(f"{dicts['url']}{dicts['ip']}")    
            return res.json()
    except Exception:
        print("Ошибка при вызове сервиса")

for key in CONFIG:
    conf_key = CONFIG[key]

    for curl in conf_key['URL']:
        report[curl] = get_resp(url=conf_key['URL'][curl], ip=IP, auth=conf_key.get('auth'))

print(json.dumps(report, indent=4))
