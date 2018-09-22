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
from pprint import pprint
import re

result=""
l1 = []
with open('nombres_por_edad_media_femeninos.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    filefem = open('femeninos.txt','w') 
    for row in spamreader:
        l1.append(row[1])
    l1sorted = sorted(l1, key=str.lower)
    for item in l1sorted:
        filefem.write(item+"\n")
    
filefem.close()
        
l2 = []
with open('nombres_por_edad_media_masculinos.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    filemasc = open('masculinos.txt','w') 
    for row in spamreader:
        l2.append(row[1])
    l2sorted = sorted(l2, key=str.lower)
    for item in l2sorted:
        filemasc.write(item+"\n")

filemasc.close()


#        print(sorted(l, key=str.lower))
#        print(row[1])
        # if re.search(r"'", row[1]):
        #     result = re.sub(r"'", "", row[1])
        # pprint(result)
