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
# This examaple creates an HDF5 file dset.h5 and an empty datasets /dset in it.
#
import h5py
#
# Create a new file using defaut properties.
#
file = h5py.File('dset.h5','w')
#
# Create a dataset under the Root group.
#
dataset = file.create_dataset("dset",(4, 6), h5py.h5t.STD_I32BE)
print("Dataset dataspace is %s" % str(dataset.shape))
print("Dataset Numpy datatype is %s" % str(dataset.dtype))
print("Dataset name is %s" % str(dataset.name))
print("Dataset is a member of the group %s" % str(dataset.parent))
print("Dataset was created in the file %s" % str(dataset.file))
#
# Close the file before exiting
#
file.close()
