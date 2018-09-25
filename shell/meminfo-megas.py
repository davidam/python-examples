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
#!/usr/bin/env python
# author: David Arroyo Menéndez
# license: gplv3

import os
f = os.popen('cat /proc/meminfo')
for line in f:
    fields = line.strip().split()
    # Array indices start at 0 unlike AWK
    if (len(fields) < 3):
        print(str(fields[0]) + " "  + str(fields[1]))
    else:
        if fields[2] == "kB":
            megas = int(fields[1]) / 1024
            print(str(fields[0]) + " " + str(megas) + " MB")
