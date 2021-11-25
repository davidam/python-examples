#!/usr/bin/python3
# -*- coding: utf-8 -*-

#  Copyright (C) 2021 David Arroyo Menéndez

#  Author: David Arroyo Menéndez <davidam@gmail.com>
#  Maintainer: David Arroyo Menéndez <davidam@gmail.com>
#  This file is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3, or (at your option)
#  any later version.
#
#  This file is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with python-examples; see the file GPL.txt.  If not, write to
#  the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
#  Boston, MA 02110-1301 USA,

import requests, sys

apikey = input('You must write the api key here: ')

print(apikey)

print("With a given doi retrieve the abstract")
abstractdoi = 'https://api.elsevier.com/content/abstract/doi/10.1016/S0014-5793(01)03313-0?apiKey=' + apikey

req_abstractdoi = requests.get(abstractdoi)

print(req_abstractdoi.url)

print("With a given doi retrieve the abstract citations")
abstractcitations = 'https://api.elsevier.com/content/abstract/citations?doi=10.1016%2FS0014-5793(01)03313-0&apiKey='+ apikey +'&httpAccept=application%2Fjson'

req_abstractcitations = requests.get(abstractcitations)

print(req_abstractcitations.url)

print("With a given eid retrieve the abstract")
abstracteid = 'https://api.elsevier.com/content/abstract/eid/2-s2.0-0037070197?apiKey=' + apikey

req_abstracteid = requests.get(abstracteid)

print(req_abstracteid.url)

abstractpii = 'https://api.elsevier.com/content/abstract/pii/S0014579301033130?apiKey=' + apikey

req_abstractpii = requests.get(abstractpii)

print(req_abstractpii.url)

abstractpubmed = 'https://api.elsevier.com/content/abstract/pubmed_id/11852050?apiKey=' + apikey

req_abstractpubmed = requests.get(abstractpubmed)

print(req_abstractpubmed.url)

abstractpui = 'https://api.elsevier.com/content/abstract/pui/34164449?apiKey=' + apikey

req_abstractpui = requests.get(abstractpui)

print(req_abstractpui.url)
