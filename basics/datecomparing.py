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

import datetime
import time

print('Times:')
t1 = datetime.time(12, 55, 0)
print('\tt1:', t1)
t2 = datetime.time(13, 5, 0)
print('\tt2:', t2)
print('\tt1 < t2:', t1 < t2)

print('Dates:')
d1 = datetime.date.today()
print('\td1:', d1)
d2 = datetime.date.today() + datetime.timedelta(days=1)
print('\td2:', d2)
print('\td1 > d2:', d1 > d2)
