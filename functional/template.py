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
class CGImethod(object):
    def __init__(self, title):
        self.title = title
    def __call__(self, fn):
        def wrapped_fn(*args):
            print("Content-Type: text/html\n\n")
            print("<HTML>")
            print("<HEAD><TITLE>{}</TITLE></HEAD>".format(self.title))
            print("<BODY>")
            try:
                fn(*args)
            except Exception as e:
                print(e)
            print("</BODY></HTML>")
        return wrapped_fn

@CGImethod("Hello with Decorator")
def say_hello():
    print('<h1>Hello from CGI-Land</h1>')

say_hello()       

@CGImethod("Hello with Decorator")
def say_hello2():
    print('<h1>Hello from CGI-Land</h1>\n' '<p>and paragraph</p>')

say_hello2()    
