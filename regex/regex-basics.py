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

import re
# import regex # if you like good times
# intended to replace `re`, the regex module has many advanced
# features for regex lovers. http://p...content-available-to-author-only...n.org/pypi/regex
subject = 'Jane"" ""Tarzan12"" Tarzan11@Tarzan22 {4 Tarzan34}'
regex = re.compile(r'{[^}]+}|"Tarzan\d+"|(Tarzan\d+)')
# put Group 1 captures in a list
matches = [group for group in re.findall(regex, subject) if group]

######## The four main tasks we're likely to have ########

# Task 1: Is there a match?
print("*** Is there a Match? ***")
if len(matches)>0:
	print ("Yes")
else:
	print ("No")

# Task 2: How many matches are there?
print("\n" + "*** Number of Matches ***")
print(len(matches))

# Task 3: What is the first match?
print("\n" + "*** First Match ***")
if len(matches)>0:
	print (matches[0])

# Task 4: What are all the matches?
print("\n" + "*** Matches ***")
if len(matches)>0:
	for match in matches:
	    print (match)

# Task 5: Replace the matches
def myreplacement(m):
    if m.group(1):
        return "Superman"
    else:
        return m.group(0)
replaced = regex.sub(myreplacement, subject)
print("\n" + "*** Replacements ***")
print(replaced)

# Task 6: Split
# Start by replacing by something distinctive,
# as in Step 5. Then split.
splits = replaced.split('Superman')
print("\n" + "*** Splits ***")
for split in splits:
	    print (split)
