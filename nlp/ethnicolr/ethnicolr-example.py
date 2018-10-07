#!/usr/bin/python
# -*- coding: utf-8 -*-


import pandas as pd

from ethnicolr import census_ln, pred_census_ln


names = [{'name': 'smith'},
         {'name': 'zhang'},
         {'name': 'jackson'}]

df = pd.DataFrame(names)

print(df)

print(census_ln(df, 'name'))

print(census_ln(df, 'name', 2010))

print(pred_census_ln(df, 'name'))
