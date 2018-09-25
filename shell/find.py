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
import subprocess
import os

#os.chdir("..")
 
# Set up find command
findCMD = 'find . -name "*.pyc" -exec rm {} \;'
out = subprocess.Popen(findCMD,shell=True,stdin=subprocess.PIPE, 
                        stdout=subprocess.PIPE,stderr=subprocess.PIPE)
# Get standard out and error
(stdout, stderr) = out.communicate()
 
# Save found files to list
filelist = stdout.decode().split()
#print(filelist)
