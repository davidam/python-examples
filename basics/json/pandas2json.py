#!/usr/bin/python
# -*- coding: utf-8 -*-
import pandas as pd
import json

df = pd.DataFrame([['a', 'b'], ['c', 'd']], index=['row 1', 'row 2'], columns=['col 1', 'col 2'])
print("split: ")
print(df.to_json(orient='split'))
print("records: ")
print(df.to_json(orient='records'))
print("index: ")
print(df.to_json(orient='index'))
print("columns: ")
print(df.to_json(orient='columns'))
print("values: ")
print(df.to_json(orient='values'))
print("table: ")
print(df.to_json(orient='table'))
