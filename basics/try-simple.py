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

import os
import signal

nombre = str(input("Indica el nombre del archivo: "))

try:
    fichero = open(nombre, "r+")
except FileNotFoundError:
    print("The program has not found the file, it stops.")
    os.kill(os.getpid(), signal.SIGUSR1)

print("The program has found the file, it continues.")

a = []
a.append(int(input("Give me an element for my array: ")))
a.append(int(input("Give me another element for my array: ")))
a.append(int(input("Give me the last element for my array: ")))

try:
    print("Second element = %d" %(a[1]))
    # Throws error since there are only 3 elements in array
    print("Third element = %d" %(a[2]))
except IndexError:
    print("The program has troubles with the array indexes")
    os.kill(os.getpid(), signal.SIGUSR1)

print("The program don't have a trouble with the array indexes")

# Program to handle multiple errors with one except statement
n1 = int(input("Give me a number: "))
n2 = int(input("Give me another number: "))

try :
    m = n1 / n2
    # throws NameError if a >= 4
    print("Value of m = %s" % m)
# note that braces () are necessary here for multiple exceptions
except(ZeroDivisionError, NameError):
    print("\nThe program has troubles with the zero division")
    os.kill(os.getpid(), signal.SIGUSR1)

print("The programa has not troubles with the zero division")

try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print("We force a raise exception")
    raise  # To determine whether the exception was raised or not
