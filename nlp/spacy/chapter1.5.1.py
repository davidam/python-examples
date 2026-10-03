#!/usr/bin/python3
# -*- coding: utf-8 -*-

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

# Solved exercises from https://course.spacy.io/en/chapter1

# 1.5 Trained Pipelines: Predicting Part-of-speech Tags

import spacy

# Load the small English pipeline
nlp = spacy.load("en_core_web_sm")

# Process a text
doc = nlp("She ate the pizza")

# Iterate over the tokens
print("---------------------------------")
print("----Iterate over the tokens------")
for token in doc:
    # Print the text and the predicted part-of-speech tag
    print(token.text, token.pos_)

print("---------------------------------")
print("--Predicting Syntactic Dependencies--")
print("----Iterate over the tokens------")
for token in doc:
    print(token.text, token.pos_, token.dep_, token.head.text)
