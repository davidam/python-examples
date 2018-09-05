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

import csv
import requests
import json

fichero = open("genderapipass.txt", "r+")
contenido = fichero.readline()
#print(contenido)

with open('partial.csv') as csvfile:
    genderapireader = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(genderapireader, None)
    genderapilist = []
    for row in genderapireader:
        name = row[0]
        name = name.replace('"', '')
        r = requests.get('https://gender-api.com/get?name='+name+'&key='+contenido)
        j = json.loads(r.text)
        genderapilist.append((j['name'], j['gender']))

print(genderapilist)
