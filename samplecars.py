#!/usr/bin/python3

import json
import string
import random
from datetime import datetime
import requests

url = 'https://parseapi.back4app.com/classes/Carmodels_Car_Model_List'
headers = {
    'X-Parse-Application-Id': '7dfAzkT5nVAuR1jHzhpTNlPyUF34YXREBHPwYEly', # This is your app's application id
    'X-Parse-REST-API-Key': '4KXLzPeO3vBTHB8dvYI96TBcLVWbu16NUph6GXKE' # This is your app's REST API key
}
cars = json.loads(requests.get(url, headers=headers).content.decode('utf-8')) # Here you have the data that you need

with open("carsample.json", "w") as write_file:
    json.dump(cars['results'], write_file)
