#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from pprint import pprint
import pandas as pd
from pandas.io.json import json_normalize
data = [
  {
    'name': {
      'first': 'vikash',
      'last': 'singh'
    },
    'age': 27
  },
  {
    'name': {
      'first': 'satyam',
      'last': 'singh'
    },
    'age': 14
  }
]

df = pd.DataFrame.from_dict(json_normalize(data), orient='columns')
print(df)
print(json_normalize(data))

jsondata = open('perceval.json').read()
json_object = json.loads(jsondata)
print(json_object)
