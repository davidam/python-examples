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


from pattern.en import verbs, conjugate, PARTICIPLE

print('google')  in verbs.infinitives
print('googled') in verbs.inflections

print(conjugate('googled', tense=PARTICIPLE, parse=False))
print(conjugate('googled', tense=PARTICIPLE, parse=True))

from pattern.en import quantify

print(quantify(['goose', 'goose', 'duck', 'chicken', 'chicken', 'chicken']))
print(quantify({'carrot': 100, 'parrot': 20}))
print(quantify('carrot', amount=1000))


from pattern.en import quantify

print(quantify(['goose', 'goose', 'duck', 'chicken', 'chicken', 'chicken']))
print(quantify({'carrot': 100, 'parrot': 20}))
print(quantify('carrot', amount=1000))

from pattern.en import ngrams
print(ngrams("I am eating pizza.", n=2)) # bigrams


from pattern.en import parse
print(parse('I ate pizza.').split())


from pattern.en import parsetree

s = parsetree('The cat sat on the mat.', relations=True, lemmata=True)
print(repr(s))

for sentence in s:
    for chunk in sentence.chunks:
        print(chunk.type), [(w.string, w.type) for w in chunk.words]


from pattern.en import sentiment

print(sentiment(
    "The movie attempts to be surreal by incorporating various time paradoxes,"
    "but it's presented in such a ridiculous way it's seriously boring."))

print(sentiment('Wonderfully awful! :-)').assessments)
