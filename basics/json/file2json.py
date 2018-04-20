#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

jsondata = open('exer1-interface-data.json').read()
json_object = json.loads(jsondata)
print(json_object)

with open('exer1-interface-data.json') as json_data:
    d = json.load(json_data)
    print(d)


