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
# This example creates an HDF5 file group.h5 and a group MyGroup in it 
# using H5Py interfaces to the HDF5 library. 
#
import sys
import h5py

# Uncomment the next line if you want to save the output from this script to a file named "out".
#sys.stdout = open('out', 'w')
#
# Use 'w' to remove existing file and create a new one; use 'w-' if
# create operation should fail when the file already exists.
#
print("Creating an HDF5 file with the name group.h5...")
file = h5py.File('group.h5','w')
#
# Show the Root group which is created when the file is created.
#
print("When an HDF5 file is created, it has a Root group with the name '",file.name,"'.")
#
# Create a group with the name "MyGroup"
#
print("Creating a group MyGroup in the file...")
group = file.create_group("MyGroup")
# 
# Print(the content of the Root group
#
print("An HDF5 group is a container for other objects; a group is similar to Python dictionary with the keys being the links to the group members.")
print("Show the members of the Root group using dictionary key method:", file.keys())
#
# Another way to show the content of the Root group.
print("Show the members of the Root group using the list function:", list(file))
#
# Close the file before exiting; H5Py will close the group.
#
file.close()
