#!/usr/bin/env python
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

import os
f = os.popen('ls -l')
for line in f:
    fields = line.strip().split()
    # Array indices start at 0 unlike AWK
    if (len(fields) == 2):
        print(line)
    else:
        megas = int(fields[4]) / 1024 / 1024
        print(fields[0] + " " + fields[1] + " " + fields[2] + " " + fields[3] + " " + str(megas) + " MB " + fields[5] + " " + fields[6] + " " + fields[7] + " " + fields[8])

