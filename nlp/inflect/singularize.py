#  Copyright (C) 2026 David Arroyo Menéndez

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
#  along with python-examples; see the file LICENSE.txt.  If not, write to
#  the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
#  Boston, MA 02110-1301 USA,


# Program to singularize a given word in Python

# Import the libraries
import inflect

# Declare method of inflect module
p = inflect.engine()

# Define the string and store it in variable
a = 'children'
b = 'apples'
c = 'men'
d = 'women'
e = 'people'
f = 'teeth'

# Print the singular of the string defined
print("Singular of children: ", p.singular_noun(a))
print("Singular of apples: ", p.singular_noun(b))
print("Singular of men: ", p.singular_noun(c))
print("Singular of women: ", p.singular_noun(d))
print("Singular of person: ", p.singular_noun(e))
print("Singular of teeth: ", p.singular_noun(f))
