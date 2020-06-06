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
# along with python-examples; see the file LICENSE.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

# here i import the module that implements regular expressions
import re

m = re.match(r"(\w+) (\w+) (\w+)", "Isaac Newton physicist")
print(m.group(0))
print(m.group(1))

r0 = re.match(r"([\w+ ]*)<([\w\.\+\-]+\@[\w]+\.[a-z]{2,3})>", "David Arroyo Menéndez <davidam@gnu.org>")
print(r0.group(0))
fullname = r0.group(1)
print("Full name: %s" % fullname)
email = r0.group(2)
print("Email: %s" % email)

# r1 = re.match(r"(\w )+(<[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}>)", "David Arroyo Menéndez <davidam@gnu.org>")
# print(r1.group(0))
# print(r1.group(1))
# print(r1.group(4))

# # here is my function to check for valid email address
def test_email(your_pattern):
    pattern = re.compile(your_pattern)
    # pattern = re.compile(.* .*@.*\.[a-z][a-z]|[a-z])
    # here is an example list of email to check it at the end
    emails = ["john@example.com", "python-list@python.org", "wha.t.`1an?ug{}ly@email.com"]
    for email in emails:
        if not re.match(pattern, email):
            print("You failed to match %s" % (email))
        elif not your_pattern:
            print("Forgot to enter a pattern!")
        else:
            print("Pass")
            
# # my pattern that is passed as argument in my function is here!
pattern = r"[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}"
# pattern = r"(.*) ([\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$)"
# #pattern = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"
# # here i test my function passing my pattern
test_email(pattern)
