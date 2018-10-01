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

import json

class SimpleClass:
    def __init__(self, a=None, b=None, c=None):
        self.a = a
        self.b = b
        self.c = c

def serialize_json(instance=None, path=None):
    dt = {}
    dt.update(vars(instance))

    with open(path, "w") as file:
        json.dump(dt, file)

def deserialize_json(cls=None, path=None):
    def read_json(_path):
        with open(_path, "r") as file:
            return json.load(file)

    data = read_json(path)

    instance = object.__new__(cls)

    for key, value in data.items():
        setattr(instance, key, value)

    return instance

# Usage: Create class and serialize under Windows file system.
write_settings = SimpleClass(a=1, b=2, c=3)
serialize_json(write_settings, r"object.json")

# Read back and rehydrate.
read_settings = deserialize_json(SimpleClass, r"object.json")

print("The object is written in object.json")
