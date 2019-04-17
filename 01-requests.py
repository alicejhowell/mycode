#!/usr/bin/python3
import requests
majortom = requests.get('http://api.open-notify.org/astros.json')
print(majortom)
