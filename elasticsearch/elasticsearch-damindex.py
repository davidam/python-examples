from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()

# doc = {
#     'author': 'kimchy',
#     'text': 'Elasticsearch: cool. bonsai cool.',
#     'timestamp': datetime.now(),
# }

# res = es.index(index="dam-index", doc_type='item', id=1, body=doc)
# #print(res['created'])

# res = es.get(index="dam-index", doc_type='item', id=1)
# print(res['_source'])

# es.indices.refresh(index="dam-index")

res = es.search(index="dam-index", body={"query": {"match_all": {}}})
print("Got %d Hits:" % res['hits']['total'])
for hit in res['hits']['hits']:
    print(hit["_source"])


