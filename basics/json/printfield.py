#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from pprint import pprint

jsondata = open('perceval.json').read()
json_object = json.loads(jsondata)
#json = json_object.dumps()
perceval = json_object["perceval"]
pprint(json_object)
print(
    "=======================================================================================" "\n"
    "Backend Name       Backend Version    Category           Author                   Message \n" 
    "----------------   -----------------  ----------------- --------------------   ----------  ------")

for i in perceval:
    print("%s               %s              %s                %s                     %s  " % (i['backend_name'], i['backend_version'], i['category'], i['data']['Author'], i['data']['message']))


print("Take care with the json format!!")
