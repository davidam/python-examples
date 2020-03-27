#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('name',  help="Name to be detected")

args = parser.parse_args()


import requests

sparql_query = """
        prefix schema: <http://schema.org/>
        SELECT ?item ?occupation ?genderLabel ?bdayLabel
        WHERE {
            <https://en.wikipedia.org/wiki/"""+ args.name +"""> schema:about ?item .
            ?item wdt:P106 ?occupation .
            ?item wdt:P21 ?gender .
            ?item wdt:P569 ?bday .
            SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
        }
    """
url = 'https://query.wikidata.org/sparql'

# sleep(2)
r = requests.get(url, params={'format': 'json', 'query': sparql_query})

url = 'https://query.wikidata.org/sparql'

r = requests.get(url, params={'format': 'json', 'query': sparql_query})
data = r.json()

print(data['results']['bindings'][0]['genderLabel']['value'])
