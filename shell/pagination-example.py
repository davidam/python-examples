#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2020  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@libresoft>
# Maintainer: David Arroyo Menéndez <davidam@libresoft>

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with python-examples; see the file LICENSE.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, 
# Boston, MA 02110-1301 USA,

from __future__ import print_function

import subprocess, tempfile

page = True  # For tests

# Definition of a printc() function that prints to the correct output
if page:
    tmp_file = open(tempfile.mkstemp()[1], 'w')  # No need to store the name in a specific variable
    def printc(*largs, **kwargs):
        if 'file' not in kwargs:  # The code can still use the usual file argument of print()
            kwargs['file'] = tmp_file  # Forces the output to go to the temp file
        print(*largs, **kwargs)
else:
    printc = print  # Regular print

# Main program:

printc('...some text...', 'some more text', sep='/')  # Python3 syntax

# Paging of the current contents of the temp file:
if page:
    tmp_file.flush()  # No need to close the file: you can keep printing to it
    subprocess.call(['less', tmp_file.name])  # Simpler than a full Popen()
