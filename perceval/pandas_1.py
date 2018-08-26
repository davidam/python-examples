#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## Copyright (C) 2017 Bitergia
##
## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 3 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
##
## Authors:
##   Jesus M. Gonzalez-Barahona <jgb@bitergia.com>
##
## Some simple examples for exploring how to work with pandas
## and GrimoireLab indexes.

from datetime import datetime

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
import pandas as pd

es = Elasticsearch('http://localhost:9200', verify_certs=False)

# Buckets by author name, finding first commit for each of them
s = Search(using=es, index='git')
s.aggs.bucket('by_authors', 'terms', field='author', size=10000) \
    .metric('commited_date', 'min', field='authored_date')
s = s.sort("authored_date")
result = s.execute()

# Uncomment the following two lines to see the resutls obtained
# from the query
from pprint import pprint
# pprint(result.to_dict())

# Get a dataframe with each author and their first commit
buckets_result = result['aggregations']['by_authors']
pprint(buckets_result)
buckets = []
for bucket in buckets_result:
    pprint(bucket)
    break
#    commited_date = bucket['commited_date']['value']/1000
    # commited_date = bucket['commited_date']/1000
    # buckets.append(
    #     {'commited_date': datetime.utcfromtimestamp(commited_date),
    #     'author': bucket['key']}
    #     )
#authors = pd.DataFrame.from_records(buckets)
#authors.sort_values(by='commited_date', ascending=False, inplace=True)

# # Uncomment the following line (and the import of pprint, above)ç
# # to print the dataframe
# #pprint(authors)

# # Get number of new authors per month
# by_month = authors['first_commit'] \
#     .groupby([authors.first_commit.dt.year,
#             authors.first_commit.dt.month]) \
#     .agg('count')

# #pprint(by_month)

# # Produce csv files
# print("Creating CSV for new authors per month.")
# by_month.to_csv('authors_per_month.csv')
# print("Creating CSV for first date for authors.")
# authors.to_csv('authors_first.csv',
#                 columns=['first_commit', 'author'],
#                 index=False)
