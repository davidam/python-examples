#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2020  David Arroyo Menéndez

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
# along with python-examples; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,
#from random import shuffle

import random

dice1 = ["fuck", "suck", "finger", "feet", "caress", "blow"]
dice2 = ["tit", "pussy", "ass", "mouth", "cock", "pussy"]

random.shuffle(dice1,random.random)
random.shuffle(dice2,random.random)
print(dice1[0])
print(dice2[0])

# print(shuffle(dice1))
# print(shuffle(dice2))

# from random import shuffle
# x = [[i] for i in range(10)]
# shuffle(x)


# import random

# list = [20, 16, 10, 5];
# random.shuffle(list)
# print ("Reshuffled list : ",  list)

# dice1 = ["fuck", "suck", "finger", "feet", "caress", "blow"]
# #dice2 = ["tit", "pussy", "ass", "mouth", "cock", "pussy"]

# print(random.shuffle(dice1))


# random.shuffle(list)
# print ("Reshuffled list : ",  list)
