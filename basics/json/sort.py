#!/bin/env python
#coding: utf8

import sys
import os
import json
import operator


#load json from file
jsondata = open('exer1-interface-data.json').read()
json_obj = json.loads(jsondata)

#sort json
lines = sorted(lines, key=lambda k: k['clients']['age'], reverse=True)

#output result
for line in lines:
    print(line)
