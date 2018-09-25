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

import sys
import re

output = "noblank"

if len(sys.argv) == 2:
    arg1 = sys.argv[1]
else:
    print("You must give an input file")
    exit()

fo = open(arg1, "r")
print("Name of the input file: %s", fo.name)
print("Name of the output file: %s", output)

lines_seen = set() # holds lines already seen
outfile = open(output, "w")

for line in open(fo.name, "r"):
    print(line)
    if not(re.match(r'^\s*$', line)):
        print(line)
        outfile.write(line)
outfile.close()
