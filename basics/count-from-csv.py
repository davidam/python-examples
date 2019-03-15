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


with open('2017girlsnames-uk.csv') as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=['Count3']) #, delimiter=',', quotechar='|')
    count = 0
    for row in reader:
        try:
            i = int(row['Count3'])
        except ValueError:
            i = 0
        count = count + i

print("Girls in UK: " + str(count))

with open('2017boysnames-uk.csv') as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=['Count3']) #, delimiter=',', quotechar='|')
    count = 0
    for row in reader:
        try:
            i = int(row['Count3'])
        except ValueError:
            i = 0
        count = count + i

print("Boys in UK: " + str(count))


# print(count)
#        print(sorted(l, key=str.lower))
#        print(row[1])
        # if re.search(r"'", row[1]):
        #     result = re.sub(r"'", "", row[1])
        # pprint(result)
