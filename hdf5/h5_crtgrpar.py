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
# This example creates HDF5 file group.h5 and group MyGroup in it.
# Absolute and relative paths are used to create groups in MyGroup. 
#
import sys
import h5py

#
# Use 'w' to remove existing file and create a new one; use 'w-' if
# create operation should fail when the file already exists.
#
print("Creating HDF5 file group.h5...")
file = h5py.File('group.h5','w')
#
# Create a group with the name "MyGroup"
#
print("Creating group MyGroup in the file...")
group = file.create_group("MyGroup")
#
# Create group "Group_A" in group MyGroup
#
print("Creating group Group_A in MyGroup using absolute path...")
group_a = file.create_group("/MyGroup/Group_A")
#
# Create group "Group_B" in group MyGroup
#
print("Creating group Group_B in MyGroup using relative path...")
group_b = group.create_group("Group_B")
# 
# Print the contents of MyGroup group
#
print("Printing members of MyGroup group: %s " % str(group.keys()))
#
# Close the file before exiting; H5Py will close the groups we created.
#
file.close()
