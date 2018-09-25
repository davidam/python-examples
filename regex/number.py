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
import os, re

num = input("Write a number: ")

print("Is it your number from 1 to 12? ")
match = re.search(r'^(1[0-2]|[1-9])$', num)
# If-statement after search() tests if it succeeded
if match:                      
    print("Yes, it's") # match.group() ## 'found word:cat'
else:
    print("Not, it isn't")

print("Is it your number from 1 to 24? ")
match = re.search(r'^(2[0-4]|1[0-9]|[1-9])$', num)
# If-statement after search() tests if it succeeded
if match:                      
    print("Yes, it's") # match.group() ## 'found word:cat'
else:
    print("Not, it isn't")

print("Is it your number from 1 to 31? ")
match = re.search(r'^(3[01]|[12][0-9]|[1-9])$', num)
# If-statement after search() tests if it succeeded
if match:                      
    print("Yes, it's") # match.group() ## 'found word:cat'
else:
    print("Not, it isn't")

print("Is it your number from 1 to 53? ")
match = re.search(r'^(5[0123]|[1-4][0-9]|[1-9])$', num)
# If-statement after search() tests if it succeeded
if match:                      
    print("Yes, it's") # match.group() ## 'found word:cat'
else:
    print("Not, it isn't")

print("Is it your number from 0 to 59? ")
match = re.search(r'^([1-5][0-9]|[0-9])$', num)
# If-statement after search() tests if it succeeded
if match:                      
    print("Yes, it's") # match.group() ## 'found word:cat'
else:
    print("Not, it isn't")

print("Is it your number from 0 to 100? ")
match = re.search(r'^([1]?[0-9]?[0-9])$', num)
if match:                      
    print("Yes, it's") # match.group() ## 'found word:cat'
else:
    print("Not, it isn't")

print("Is it your number from 1 to 100? ")
match = re.search(r'^(100|[1-9][0-9]|[1-9])$', num)
if match:                      
    print("Yes, it's") # match.group() ## 'found word:cat'
else:
    print("Not, it isn't")
    
print("Is it your number from 32 to 126? ")
match = re.search(r'^(12[0-6]|1[0-1][0-9]|[4-9][0-9]|3[2-9])$', num)
if match:                      
    print("Yes, it's") # match.group() ## 'found word:cat'
else:
    print("Not, it isn't")
