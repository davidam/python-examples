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
# This examaple creates and writes two attributes on the "dset" dataset created by h5_crtdat.py.
#
import h5py
import numpy as np
#
# Open an existing file using defaut properties.
#
file = h5py.File('dset.h5','r+')
#
# Open "dset" dataset.
#
dataset = file['/dset']
#
# Create string attribute.
#
attr_string = "Meter per second"
dataset.attrs["Units"] = attr_string
#
# Create integer array attribute.
#
attr_data = np.zeros((2))
attr_data[0] = 100
attr_data[1] = 200
#
#
dataset.attrs.create("Speed", attr_data, (2,), h5py.h5t.STD_I32BE)
#
# Close the file before exiting
#
file.close()
