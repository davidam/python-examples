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

import math

# Return the ceiling of x as a float, the smallest integer value greater than or equal to x.
print(math.ceil(-9))

# Return x with the sign of y. On a platform that supports signed zeros, copysign(1.0, -0.0) returns -1.0.
print(math.copysign(-2, 2))

# Return the absolute value of x.
print(math.fabs(-3))

# Return x factorial. Raises ValueError if x is not integral or is negative.
print(math.factorial(3))

# Return fmod(x, y), as defined by the platform C library.
print(math.fmod(3, 2))

# Return the mantissa and exponent of x as the pair (m, e).
print(math.frexp(4))

# Return an accurate floating point sum of values in the iterable.
print(sum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]))
print(math.fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]))

# Check if the float x is positive or negative infinity.
print(math.isinf(-10.0))

# Check if the float x is a NaN (not a number).
print(math.isnan(34.2))

# Return x * (2**i).
print(math.ldexp(2, 3))

# Return the fractional and integer parts of x.
print(math.modf(4))

# Return the Real value x truncated to an Integral (usually a long integer).
print(math.trunc(3.2))

#################### POWER AND LOGARITHMIC FUNCTIONS #######################

from math import exp, expm1

print(exp(1e-5) - 1)
print(expm1(1e-5))
print(math.log(4,2))
print(math.log1p(11))
print(math.log10(100))
print(math.pow(2, 3))
print(math.sqrt(25))

################### TRIGONOMETRIC FUNCTIONS ###############################

a = math.pi/6

# returning the value of sine of pi/6
print("The value of sine of pi/6 is : ", end="")
print(math.sin(a))

# returning the value of cosine of pi/6
print("The value of cosine of pi/6 is : ", end="")
print(math.cos(a))

a = math.pi/6
b = 3
c = 4

# returning the value of tangent of pi/6
print("The value of tangent of pi/6 is : ", end="")
print(math.tan(a))

# returning the value of hypotenuse of 3 and 4
print("The value of hypotenuse of 3 and 4 is : ", end="")
print(math.hypot(b,c))
# print(math.acos(math.radians(45)))
# print(math.acos(math.radians(90)))
# print(math.acos(math.radians(135)))
# print(math.acos(math.radians(180)))
# print(math.acos(0))
# print(math.acos(45))
# print(math.acos(90))

#################### CONSTANTS #############################################

print(math.pi)
print(math.e)
