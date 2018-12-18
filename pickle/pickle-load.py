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
import pprint, pickle

pkl_file = open('data.pkl', 'rb')

data1 = pickle.load(pkl_file)
pprint.pprint(data1)

data2 = pickle.load(pkl_file)
pprint.pprint(data2)

pkl_file2 = open('finalized_model.sav', 'rb')
data3 = pickle.load(pkl_file2)
pprint.pprint(data3)

pkl_file3 = open('bernoulliNB_model.sav', 'rb')
data4 = pickle.load(pkl_file3)
pprint.pprint(data4)

pkl_file4 = open('gaussianNB_model.sav', 'rb')
data5 = pickle.load(pkl_file4)
pprint.pprint(data5)

pkl_file5 = open('multinomialNB_model.sav', 'rb')
data6 = pickle.load(pkl_file5)
pprint.pprint(data6)


pkl_file.close()
pkl_file2.close()
