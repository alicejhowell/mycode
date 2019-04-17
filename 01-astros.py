#!/usr/bin/python3
import urllib.request
import json

def main():
    majortom = urllib.request.urlopen('http://api.open-notify.org/astros.json')
    helmetson = majortom.read().decode('utf-8')
    groundctrl = json.loads(helmetson)

    for astro in groundctrl['people']:
        print(astro['name'])

main()    
