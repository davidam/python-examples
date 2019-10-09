#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2019  David Arroyo Menéndez

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
# along with n3; see the file LICENSE.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

# Serializing a single term to N3

from rdflib import Graph, URIRef, Literal, BNode
from rdflib.namespace import FOAF, NamespaceManager

person = URIRef('http://xmlns.com/foaf/0.1/Person')
print(person.n3())

g = Graph()
print(g.bind("foaf", FOAF))

print(person.n3(g.namespace_manager))

l = Literal(2)
print(l.n3())

print(l.n3(g.namespace_manager))
