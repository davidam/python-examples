#!/usr/bin/python
# -*- coding: utf-8 -*-

import elasticsearch
from elasticsearch_dsl import Q

INIT_DATE_4Y = '2013-10-01'
INIT_DATE_1Y = '2016-10-01'
END_DATE = '2017-10-01'

INDEX = "gerrit_eventized"
filter_date_4y = Q('range', date={'gte': INIT_DATE_4Y, 'lt': END_DATE})
filter_date_1y = Q('range', date={'gt': INIT_DATE_1Y, 'lt': END_DATE})

print(filter_date_4y)
print(filter_date_1y)
