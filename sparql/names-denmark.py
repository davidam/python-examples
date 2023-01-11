#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2019  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with python-examples; see the file LICENSE.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

import requests
from SPARQLWrapper import SPARQLWrapper, JSON

#'Master of the Drapery Studies'

url = 'https://query.wikidata.org/sparql'
# query = """
# SELECT ?human ?humanLabel
# WHERE
# {
# 	?human 'Master of the Drapery Studies' ?humanLabel
# 	SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en" }
# }
# limit 20
# """

female = True

if female:
    gender = "    ?person wdt:P21 wd:Q6581072 . "
elif male:
    gender = "    ?person wdt:P21 wd:Q6581097 . "

query2 = """
SELECT ?name ?nameLabel ?count
WITH {
  SELECT ?name (count(?person) AS ?count) WHERE {
    ?person wdt:P735 ?name .
""" + gender + """
    ?person wdt:P27 wd:Q35 .
  }
  GROUP BY ?name
  ORDER BY DESC(?count)
  LIMIT 100
} AS %results
WHERE {
  INCLUDE %results
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
ORDER BY DESC(?count)
"""

def get_results(endpoint_url, query):
    sparql = SPARQLWrapper(endpoint_url)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()


results = get_results(url, query2)

print("Dumping results to names-denmark.csv")

fo = open("names-denmark.csv", "w")
for result in results["results"]["bindings"]:
    fo.write(result['nameLabel']['value'] + "," + result['count']['value'] +  "\n");

# Cerramos el archivo fichero.txt
fo.close()


# r = requests.get(url, params = {'format': 'json', 'query': query2})
# data = r.json()
# print(data)

r = requests.get(url, params = {'format': 'json', 'query': query2})
data = r.json()

print(data["results"]["bindings"])

fo = open("names-denmark.csv", "w")
for d in data["results"]["bindings"]:
    print(d)
    print(d["count"]["value"])
    print(d["nameLabel"]["value"])
    fo.write(d['nameLabel']['value'] + "," + d['count']['value'] +  "\n")

# Cerramos el archivo fichero.txt
fo.close()
