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

print("I am a girl, I like your programming style. I can give you a contract.")
print("How long is the project?")
print("Undefined, I am the boss of an important startup. You must work very close to me. I will know when is finished the project.")
a = input("Do you accept? ( Y | N ): ")
if ( a == "Y" ):
    count = 0
    while (count < 9):
        print("Week: %s" % (str(count)))
        print("Fixing bugs, reaching tasks")
        count = count + 1
    print("Ok, we are in a critical moment. We must do a walk.")
    a2 = input("Do you accept? ( Y | N ): ")
    if (a2 == "Y"):
        print("Ok, the walk is ok. I am so happy. The project is finished. You tourist can come back to home.")
