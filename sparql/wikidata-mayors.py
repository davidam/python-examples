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
# along with wikidata-mayors; see the file LICENSE.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

import requests

url = 'https://query.wikidata.org/sparql'
query="""
SELECT DISTINCT
  ?countryLabel ?capitalLabel ?population ?capital_lon ?capital_lat
  ?mayorLabel ?birth_date ?age ?birth_place ?birth_placeLabel ?birth_place_lon ?birth_place_lat
WHERE {
  ?country wdt:P463 wd:Q458.
  ?country wdt:P36 ?capital.
  OPTIONAL { ?capital wdt:P1082 ?population. }

  # Get latitude longitude coordinates of capital
  ?capital p:P625/psv:P625 ?capital_node.
  ?capital_node wikibase:geoLatitude ?capital_lat.
  ?capital_node wikibase:geoLongitude ?capital_lon.

  ?capital p:P6 ?statement.
  ?statement ps:P6 ?mayor.
  FILTER NOT EXISTS { ?statement pq:P582 ?end_date }

  ?mayor wdt:P569 ?birth_date.
  BIND(year(now()) - year(?birth_date) AS ?age)
  ?mayor wdt:P19 ?birth_place.
  ?birth_place wdt:P625 ?birth_place_coordinates.

  # Get latitude longitude coordinates of birth place
  ?birth_place p:P625/psv:P625 ?birth_place_node.
  ?birth_place_node wikibase:geoLatitude ?birth_place_lat.
  ?birth_place_node wikibase:geoLongitude ?birth_place_lon.

  SERVICE wikibase:label {
    bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en".
  }
}
"""

r = requests.get(url, params = {'format': 'json', 'query': query})
data = r.json()
print(data)

import pandas as pd
from collections import OrderedDict

countries = []
for item in data['results']['bindings']:
    countries.append(OrderedDict({
        label : item[label]['value'] if label in item else None
        for label in ['countryLabel', 'capitalLabel',  'capital_lon', 'capital_lat', 'population',
                      'mayorLabel', 'birth_date', 'age',
                      'birth_placeLabel', 'birth_place_lon', 'birth_place_lat']}))

df = pd.DataFrame(countries)
df.set_index('capitalLabel', inplace=True)
df = df.astype({'population': float, 'age': float,
                'capital_lon': float, 'capital_lat': float,
                'birth_place_lon': float, 'birth_place_lat': float})

print(df.head())
