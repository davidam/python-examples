#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2018  David Arroyo Menéndez

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

import time
from datetime import date
import json
import regex as re

merge = []

with open('data11.json') as json_data:
    d = json.load(json_data)
    for i in d:
        datesec = round(i["d"]/1000)
        dateformat = date.fromordinal(datesec)
        diccionario = {}
        diccionario['date'] = dateformat.strftime("%Y-%m-%d")
        diccionario['cat'] = i['cat'].upper()
        diccionario['value'] = i['value']
#        print(diccionario)
        merge.append(diccionario)

with open('data2.json') as json_data:
    d = json.load(json_data)
    print(d)
    d2 = date.fromordinal(datesec)
    print(d2.strftime("%Y/%m/%d"))
    print(d[0]['categ'])
    print(d[0]['myDate'])
    print(d[0]['val'])
    diccionario = {}
    for j in d:
        diccionario['date'] = j['myDate']
        diccionario['cat'] = j['categ'].upper()
        diccionario['value'] = j['val']
        merge.append(diccionario)

with open('data3.json') as json_data:
    d = json.load(json_data)
#    print(d)
    for z in d:
        datereg = re.search(r'\b(\d\d\d\d)-(\d\d)-(\d\d)\b', z['raw'])
        catreg = re.search(r'#(?P<cat>.*)#', z['raw'])
        if datereg:
            diccionario['date'] = datereg.group()
        else:
            print("did not find")
        if catreg:
            diccionario['cat'] = catreg.group('cat').upper()
        else:
            print("did not find")
        diccionario['value'] = z['val']
        merge.append(diccionario)

print("##############  JSON  ################")
print(merge)

file = open("merge.json", "w")
for m in merge:
    file.write(str(m) + "\n")

file.close()

ncat1 = 0
ncat2 = 0
ncat3 = 0

for m in merge:
    if (m['cat'] == 'CAT 1'):
        ncat1 = ncat1 + m['value']
    elif (m['cat'] == 'CAT 2'):
        ncat2 = ncat2 + m['value']
    elif (m['cat'] == 'CAT 3'):
        ncat3 = ncat3 + m['value']

print("CAT 1: " + str(round(ncat1)))
print("CAT 2: " + str(round(ncat2)))
print("CAT 3: " + str(round(ncat3)))
