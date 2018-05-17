#!/usr/bin/python
# -*- coding: utf-8 -*-
from elasticsearch_dsl import Search, Q
#from util import ESConnection
import pandas as pd

class Query(object):
    def query_metric_over_time(index, metric_name, metric_field, filters = []):
        s = Search(using=es_conn, index=index)  # Index selection
        for filtering in filters:
            s = s.filter(filtering)
            s.aggs.bucket('gender', 'terms', field='gender')\
                  .bucket('time', 'date_histogram', field='date', interval='quarter')\
                  .metric(metric_name, 'cardinality', field=metric_field, precision_threshold=10000)
            result = s.execute()

            value = result.to_dict()["aggregations"]['gender']['buckets']
    
            df = pandas.DataFrame()
            for i in value:
                df2 = (pandas.DataFrame.from_dict(i["time"]["buckets"]))
                df2["gender"] = i["key"]
                df2[metric_name] = df2[metric_name].apply(lambda row:row["value"])
                df = pandas.concat([df, df2])
        return df

#es_conn = ESConnection()    
INIT_DATE_4Y = '2013-10-01'
INIT_DATE_1Y = '2016-10-01'
END_DATE = '2017-10-01'
    
INDEX = "gerrit_openstack_gender_uuids"
filter_date_4y = Q('range', date={'gte': INIT_DATE_4Y, 'lt': END_DATE})
print(filter_date_4y)
filter_date_1y = Q('range', date={'gte': INIT_DATE_1Y, 'lt': END_DATE})
print(filter_date_1y)

METRIC_NAME = "changesets"
METRIC_FIELD = "id"
filter_changeset_submission = Q('term', eventtype='CHANGESET_SENT') # filter by event: vote a code review
print(filter_changeset_submission)

q = Query()
f = [filter_date_4y, filter_changeset_submission]
df = q.query_metric_over_time(INDEX, METRIC_NAME, METRIC_FIELD, f)
