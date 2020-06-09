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
# along with ; see the file LICENSE.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

from http import cookies
C = cookies.SimpleCookie()
C["fig"] = "newton"
C["sugar"] = "wafer"
print("------------------------")
print(C) # generate HTTP headers
print("------------------------")
print(C.output()) # same thing
print("------------------------")
C = cookies.SimpleCookie()
C["rocky"] = "road"
C["rocky"]["path"] = "/cookie"
print(C.output(header="Cookie:"))
print("------------------------")
print(C.output(attrs=[], header="Cookie:"))
C = cookies.SimpleCookie()
C.load("chips=ahoy; vienna=finger") # load from a string (HTTP header)
print("------------------------")
print(C)
print("------------------------")
C = cookies.SimpleCookie()
C.load('keebler="E=everybody; L=\\"Loves\\"; fudge=\\012;";')
print("------------------------")
print(C)
print("------------------------")
C = cookies.SimpleCookie()
C["oreo"] = "doublestuff"
C["oreo"]["path"] = "/"
print("------------------------")
print(C)
print("------------------------")
C = cookies.SimpleCookie()
C["twix"] = "none for you"
C["twix"].value
C = cookies.SimpleCookie()
C["number"] = 7 # equivalent to C["number"] = str(7)
C["string"] = "seven"
C["number"].value
C["string"].value
print("------------------------")
print(C)
print("------------------------")
