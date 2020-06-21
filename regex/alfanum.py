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

str = input("Write a string: ")

print("Is alfanumeric your string? ")
match = re.search(r'([a-z]|[A-Z]| |[0-9])', str)
# If-statement after search() tests if it succeeded
if match:
    print("Yes, it's") # match.group() ## 'found word:cat'
else:
    print("Not, it isn't")

print("It contains white spaces? ")
match = re.search(r'( )', str)
# If-statement after search() tests if it succeeded
if match:
    print("Yes, it's") # match.group() ## 'found word:cat'
else:
    print("Not, it isn't")

print("Is it an initial letter? ")
match = re.search(r'([A-Z][\.| ]){1,2}', str)
if match:
    print("Yes, it's") # match.group() ## 'found word:cat'
else:
    print("Not, it isn't")
