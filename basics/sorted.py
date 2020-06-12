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
#!/usr/bin/python# -*- coding: utf-8 -*-
# https://docs.python.org/3/howto/sorting.html

print(sorted([5, 2, 3, 1, 4]))
print(sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}))
sorted("This is a test string from Andrew".split(), key=str.lower)

student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
sorted(student_tuples, key=lambda student: student[2]) 

class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name, self.grade, self.age))

student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]
print(sorted(student_objects, key=lambda student: student.age))

# Operator Module

from operator import itemgetter, attrgetter
print("Operator Module, the original list is: ")
print(str(student_tuples))
print("itemgetter(2)")
print(sorted(student_tuples, key=itemgetter(2)))
print("attrgetter('age')")
print(sorted(student_objects, key=attrgetter('age')))
print("The operator module functions allow multiple levels of sorting. For example, to sort by grade then by age:")
print("itemgetter(1, 2)")
print(sorted(student_tuples, key=itemgetter(1,2)))
print("attrgetter('grade', 'age')")
print(sorted(student_objects, key=attrgetter('grade', 'age')))
print("itemgetter(2)")
print(sorted(student_tuples, key=itemgetter(2), reverse=True))
print("attrgetter('age')")
print(sorted(student_objects, key=attrgetter('age'), reverse=True))

# Sort Stability and Complex Sorts

data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
print("Original list")
print(data)
print("Sorted data itemgetter(0)")
print(sorted(data, key=itemgetter(0)))

# The Old Way Using Decorate-Sort-Undecorate

decorated = [(student.grade, i, student) for i, student in enumerate(student_objects)]
decorated.sort()
[print(student) for grade, i, student in decorated]

# Sort list of lists

def getKey(item):
    return item[0]

l = [[2, 3], [6, 7], [3, 34], [24, 64], [1, 43]]

print(sorted(l, key=getKey))

