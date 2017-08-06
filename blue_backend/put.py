# -*- coding: utf-8 -*-
import requests

url = "https://blue-backend.herokuapp.com/api//api/v1/payloads/"
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
json = '''{
            "Authorization": {Token 9043f2c9597e7bba9371665e62356b1cc68a2b7f},
}'''


data = {
        "data": "Ola menina",
        }
headers = {
        'Authorization': 'Token 9043f2c9597e7bba9371665e62356b1cc68a2b7f',
        "Content-Type": "application/json",
        "data": data
        }

response = requests.put(url, data=data, headers=headers)
print(response.text)
