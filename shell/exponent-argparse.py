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


import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-base", type=int,
                    help="display a base number")
parser.add_argument("-exponent", type=int,
                    help="an exponent of a given base")
parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity")
args = parser.parse_args()
# print(args.base)
# print(args.exponent)


result = args.base
for i in range(1, args.exponent):
    result = result * args.base

#print(result)    
if args.verbose:
    print("the base is {}, the exponent is {}, the result is {}".format(args.base, args.exponent, result))
else:
    print(result)
