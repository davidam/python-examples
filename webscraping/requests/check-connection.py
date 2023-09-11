#!/usr/bin/python3
# -*- coding: utf-8 -*-

#  Copyright (C) 2023 David Arroyo Menéndez

#  Author: David Arroyo Menéndez <davidam@gmail.com> 
#  Maintainer: David Arroyo Menéndez <davidam@gmail.com> 
#  This file is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3, or (at your option)
#  any later version.
# 
#  This file is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
# 
#  You should have received a copy of the GNU General Public License
#  along with python-examples; see the file GPL.txt.  If not, write to
#  the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, 
#  Boston, MA 02110-1301 USA,

import requests

try:
    r1 = requests.get('https://api.github.com/events', timeout=3)
    r1.raise_for_status()
    if r1.text:
        print("There are network connection")
        print("request.get is your friend")
except requests.exceptions.ConnectionError as errc:
    print("There are not network connection")
    print("request.get is not helping you")
 
#    print("Error Connecting:", errc)    

