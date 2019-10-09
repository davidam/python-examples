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
# along with navigating; see the file LICENSE.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

# An RDF Graph is a set of RDF triples
# We can add triples, sort triples in the graph, print by language, ...

from rdflib import ConjunctiveGraph, URIRef, RDFS, Literal
from rdflib.namespace import SKOS
from pprint import pprint
g = ConjunctiveGraph()
u = URIRef(u'http://example.com/foo')
g.add([u, RDFS.label, Literal('foo')])
g.add([u, RDFS.label, Literal('bar')])
pprint(sorted(g.preferredLabel(u)))
g.add([u, SKOS.prefLabel, Literal('bla')])
pprint(g.preferredLabel(u))
g.add([u, SKOS.prefLabel, Literal('blubb', lang='en')])
sorted(g.preferredLabel(u))
g.preferredLabel(u, lang='')
pprint(g.preferredLabel(u, lang='en'))
