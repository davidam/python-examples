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
# along with literal; see the file LICENSE.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

# Literals are the attribute values in RDF, for instance, a person’s name, the date of birth, height, etc. Literals can have a data-type (i.e. this is a double) or a language tag (this label is in English).

import datetime
from rdflib import Literal, XSD
lit2006 = Literal('2006-01-01',datatype=XSD.date)
print(lit2006.toPython())
print(lit2006 < Literal('2007-01-01',datatype=XSD.date))
print(Literal(1) > Literal(2)) # by value
print(Literal(1) > Literal(2.0)) # by value
print(Literal('1') > Literal(1)) # by DT
print(Literal('1') < Literal('1')) # by lexical form
print(Literal('a', lang='en') > Literal('a', lang='fr')) # by lang-tag
