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
# along with GNU Emacs; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

#from SPARQLWrapper import SPARQLWrapper, JSON
import requests

url = "https://query.wikidata.org/sparql"

query = """
SELECT ?name ?nombre ?sexo_o_g_nero ?sexo_o_g_neroLabel WHERE {
  ?human wdt:P31 wd:Q5.
  OPTIONAL { ?human wdt:P21 ?nombre. }
  OPTIONAL { ?human wdt:P21 ?sexo_o_g_nero. }
}
LIMIT 10"""

r = requests.get(url, params = {'format': 'json', 'query': query})
data = r.json()
print(data)

print(data['results']['bindings'])
# query2 = """
# SELECT ?human ?humanLabel
# WHERE
# {
# 	?human wdt:P21 ?gender
# 	FILTER isBLANK(?gender) .
# 	SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en" }
# }
# """

# query3 = """
# SELECT ?gender WHERE {
#   ?human wdt:P21 ?gender.
#   SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
#   ?David wdt:P735 wd:Q18057751.
# }
# """

# query4 = """
# SELECT ?human ?humanLabel ?David ?DavidLabel ?sexo_o_g_nero ?sexo_o_g_neroLabel WHERE {
#   ?human wdt:P21 ?gender.
#   SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
#   FILTER(ISBLANK(?gender))
#   ?David wdt:P735 wd:Q18057751.
#   OPTIONAL { ?David wdt:P21 ?sexo_o_g_nero. }
# }
# """
