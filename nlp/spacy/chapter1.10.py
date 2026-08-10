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

# 1.5 Trained Pipelines: Predicting Names Entities

import spacy

# Load the small English pipeline
nlp = spacy.load("en_core_web_sm")

# Process a text
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

# Iterate over the predicted entities
print("-----------------------------------")
print("Iterate over the predicted entities")
print("-----------------------------------")
for ent in doc.ents:
    # Print the entity text and its label
    print(ent.text, ent.label_)
print("-----------------------------------")
print("Tip: the spacy.explain method")
print("-----------------------------------")
print(spacy.explain("NNP"))
print(spacy.explain("GPE"))
print(spacy.explain("dobj"))
