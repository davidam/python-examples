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

import xml.etree.ElementTree as ET
from pprint import pprint

tree = ET.parse('country_data.xml')
root = tree.getroot()
#root = ET.fromstring(countrydata)

# Top-level elements
print(root.findall("."))

# All 'neighbor' grand-children of 'country' children of the top-level
# elements
print(root.findall("./country/neighbor"))

# Nodes with name='Singapore' that have a 'year' child
print(root.findall(".//year/..[@name='Singapore']"))

# 'year' nodes that are children of nodes with name='Singapore'
print(root.findall(".//*[@name='Singapore']/year"))

# All 'neighbor' nodes that are the second child of their parent
print(root.findall(".//neighbor[2]"))

for country in root.findall('country'):
     name = country.get('name')
     print(name)

for elem in root.findall(".//*[@name='Singapore']/year"):
    pprint(elem)

import xml.etree.ElementTree as ET
tree = ET.parse('country_data.xml')
for elem in tree.iter():
    print(elem)
