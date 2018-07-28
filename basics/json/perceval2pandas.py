#!/usr/bin/python
# -*- coding: utf-8 -*-
import pandas as pd
from pandas.io.json import json_normalize

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

df = pd.DataFrame.from_dict(json_normalize(json_object), orient='columns')
print(df)
print(df.index)
print("--------------------------------------------------------")
#print(df.columns.values))
print(df.values)
print(df.describe)
print(df)
