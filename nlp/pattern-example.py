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
# along with GNU Emacs; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

from pattern.en import referenced

print(referenced('university'))
print(referenced('hour'))

from pattern.en import pluralize, singularize

print(pluralize('child'))
print(singularize('wolves'))


from pattern.en import comparative, superlative

print(comparative('bad'))
print(superlative('bad'))

from pattern.en import conjugate, lemma, lexeme

print(lexeme('purr'))
print(lemma('purring'))
print(conjugate('purred', '3sg')) # he / she / it

from pattern.en import conjugate, lemma, lexeme

print(lexeme('purr'))
print(lemma('purring'))
print(conjugate('purred', '3sg')) # he / she / it

from pattern.de import gender, MALE, FEMALE, NEUTRAL
print(gender('Katze'))
print(gender('Mesa'))
