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

import json

dicc = {}
print("Diccionario original:")

dicc["david"] = {}
dicc["david"]["count"] = 10
dicc["brezo"] = {}
dicc["brezo"]["count"] = 10

print(dicc)

#print(sorted(dicc.keys(), reverse=True))
l = sorted(dicc.items(), reverse=False)

dicc2 = {}
for name, count in l:
    dicc2[name] = count

print(dicc2)

# print(dicc2["brezo"]["count"])
app_json = json.dumps(dicc)
print(app_json)
