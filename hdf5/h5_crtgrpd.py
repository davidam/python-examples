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
# Open an existing file using defaut properties.
#
file = h5py.File('group.h5','r+')
#
# Open "MyGroup" group and create dataset dset1 in it.
#
print("Creating dataset dset1 in MyGroup group...")
dataset1 = file.create_dataset("/MyGroup/dset1", (3,3), dtype = h5py.h5t.STD_I32BE) 
#
# Initialize data and write it to dset1.
#
data = np.zeros((3,3))
for i in range(3):
    for j in range(3):
        data[i][j] = j + 1	 
print("Writing data to dset1...")
dataset1[...] = data

#
# Open "MyGroup/Group_A" group and create dataset dset2 in it.
#
print("Creating dataset dset2 in /MyGroup/Group_A group...")
group = file['/MyGroup/Group_A']
dataset2 = group.create_dataset("dset2", (2,10), dtype = h5py.h5t.STD_I16LE)
#
# Initialize data and write it to dset2.
#
data = np.zeros((2,10))
for i in range(2):
    for j in range(10):
        data[i][j] = j + 1	 
print("Writing data to dset2...")
dataset2[...] = data
#
# Close the file before exiting.
#
file.close()
