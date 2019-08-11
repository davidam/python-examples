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
from pprint import pprint

# jsontext = '{"fruits": ["apple", "banana", "orange"]}'
# j = json.loads(jsontext);
# print(j)
# print(j['fruits'])

# # Open a file
# fo = open("db.json", "r+")
# print("Name of the file: ", fo.name)

# Assuming file has following 5 lines
# This is 1st line
# This is 2nd line
# This is 3rd line
# This is 4th line
# This is 5th line

# jsondata = open('db.json').read()
# print("JSONDATA")
# print(jsondata)
# json_object = json.loads(jsondata)
# print("JSON_OBJECT")
# print(json_object)

jsondata = open('jsonuk.json').read()
print("############################################# JSONDATA ####################################################")
print(jsondata)
print("############################################# JSONDATA ELEMENT ####################################################")
json_object = json.loads(jsondata)
print("JSON_OBJECT")
print(json_object)

# print(json_object2["names"][0])
# genderlist = [] 
# for i in json_object2["names"][0]:
#     print(i)
#     print(i['name'])
#     print(i['gender'])
#     genderlist.append(i['gender'])
#     # if (i['gender'] == 'female'):
#     #     genderlistbin.append
# # Close opend file
# #fo.close()
# print(genderlist)
