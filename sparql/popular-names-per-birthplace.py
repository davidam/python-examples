#!/usr/bin/python -*- coding: utf-8 -*-

# Copyright (C) 2019 David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gnu.org> Maintainer: David
# Arroyo Menéndez <davidam@gnu.org>

# This file is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with GNU Emacs; see the file COPYING.  If not, write to the
# Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

from SPARQLWrapper import SPARQLWrapper, JSON

endpoint_url = "https://query.wikidata.org/sparql"

query = """
#defaultView:BubbleChart
SELECT ?cid ?firstname (COUNT(*) AS ?count)
WHERE
{
  ?pid wdt:P19 wd:Q64.
  ?pid wdt:P735 ?cid.
  OPTIONAL {
    ?cid rdfs:label ?firstname
    FILTER((LANG(?firstname)) = "en")
  }
}
GROUP BY ?cid ?firstname
ORDER BY DESC(?count) ?firstname
LIMIT 5"""

def get_results(endpoint_url, query):
    sparql = SPARQLWrapper(endpoint_url)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()


results = get_results(endpoint_url, query)

print("showing some results")
for result in results["results"]["bindings"]:
    print(result)
