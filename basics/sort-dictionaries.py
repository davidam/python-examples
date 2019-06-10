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
# along with GNU Emacs; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

wordsFreqDict = {
    "hello": 56,
    "at" : 23 ,
    "test" : 43,
    "this" : 43
    }

# Sort Dictionary contents by keys using dict.keys()
'''
 Iterate over a sorted list of keys and select value from dictionary for each key
 and print the key value pairs in sorted order of keys
'''
print("Sort Dictionary contents by keys using dict.keys()")
for key in sorted(wordsFreqDict.keys()) :
    print(key , " :: " , wordsFreqDict[key])


# Sort Dictionary contents by keys using dict.items()
'''
 Iterate over a  list of tuple i.e. key / value pairs, sorted by default 0th index i.e. key
 and print the key value pairs in sorted order of keys
'''
print("Sort Dictionary contents by keys using dict.items()")
for elem in sorted(wordsFreqDict.items()) :
    print(elem[0] , " ::" , elem[1] )

# Sorting dictionary contents in reverse order of keys

'''
Iterate over the list of tuples sorted by 0th index i.e. value in reverse order
'''
print("Sorting dictionary contents in reverse order of keys")
for elem in sorted(wordsFreqDict.items(), reverse=True) :
    print(elem[0] , " ::" , elem[1] )

# Sort dictionary contents by key using custom key functions
print("Sort dictionary contents by key using custom key functions")
listofTuples = sorted(wordsFreqDict.items() ,  key=lambda x: len (x[0] ) )

for elem in listofTuples :
    print(elem[0] , " ::" , elem[1] )

# Sort dictionary contents by Value
print("Sort dictionary contents by Value")
# Create a list of tuples sorted by index 1 i.e. value field
listofTuples = sorted(wordsFreqDict.items() ,  key=lambda x: x[1])
for elem in listofTuples :
    print(elem[0] , " ::" , elem[1] )

# Sorting dictionary by value in reverse Order
print("Sorting dictionary by value in reverse Order")
# Create a list of tuples sorted by index 1 i.e. value field
listofTuples = sorted(wordsFreqDict.items() , reverse=True, key=lambda x: x[1])

# Iterate over the sorted sequence
for elem in listofTuples :
    print(elem[0] , " ::" , elem[1] )
