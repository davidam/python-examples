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
"""

SPARQL Query using :meth:`rdflib.graph.Graph.query`

The method returns a :class:`~rdflib.query.Result`, iterating over
this yields :class:`~rdflib.query.ResultRow` objects

The variable bindings can be access as attributes of the row objects
For variable names that are not valid python identifiers, dict access
(i.e. with ``row[var] / __getitem__``) is also possible.

:attr:`~rdflib.query.ResultRow.vars` contains the variables

"""

import rdflib

if __name__=='__main__':

    g = rdflib.Graph()
    g.load("foaf.rdf")

    # the QueryProcessor knows the FOAF prefix from the graph
    # which in turn knows it from reading the RDF/XML file
    for row in g.query(
            'select ?s where { [] foaf:knows ?s .}'):
        print(row.s)
        # or row["s"]
        # or row[rdflib.Variable("s")]
