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
#
# This example writes data to the existing empty dataset created by h5_crtdat.py and then reads it back.
#
import h5py
import numpy as np
#
# Open an existing file using default properties.
#
file = h5py.File('dset.h5','r+')
#
# Open "dset" dataset under the root group.
#
dataset = file['/dset']
#
# Initialize data object with 0.
#
data = np.zeros((4,6))
#
# Assign new values
#
for i in range(4):
    for j in range(6):
        data[i][j]= i*6+j+1	 
#
# Write data
#
print("Writing data...")
dataset[...] = data
#
# Read data back and print it.
#
print("Reading data back...")
data_read = dataset[...]
print("Printing data...")
print(data_read)
#
# Close the file before exiting
#
file.close()
